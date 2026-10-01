"""Opt-in Docker regression using prebuilt images and local network fixtures.

SCI_BENCH_NETWORK_TEST_IMAGE=<environment-image> python -m unittest \
    tests.test_network_policy_e2e -v
"""

from __future__ import annotations

import asyncio
import json
import os
import subprocess
import tempfile
import unittest
import uuid
from pathlib import Path

from pier.models.agent.network import NetworkAllowlist
from pier.models.task.config import EnvironmentConfig
from pier.models.trial.paths import TrialPaths

from scripts.pier_network import ScienceBenchDocker


SERVER = """
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import threading
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'network-fixture-ok')
    def log_message(self, *args): pass
for port in (80, 4000):
    server = ThreadingHTTPServer(('0.0.0.0', port), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
threading.Event().wait()
"""


PROBES = """
import json, os, socket, subprocess
results=[]
def probe(name, url, expected, options=(), cleared=False):
    env=dict(os.environ)
    if cleared:
        for k in ('HTTP_PROXY','HTTPS_PROXY','ALL_PROXY','NO_PROXY','http_proxy','https_proxy','all_proxy','no_proxy'):
            env[k]=''
    p=subprocess.run(['curl','-sS','--connect-timeout','2','--max-time','4','-w','\\n%{http_code}',*options,url],
                     capture_output=True,text=True,env=env,timeout=7)
    status=p.stdout.rsplit('\\n',1)[-1]
    if expected=='allowed':
        assert p.returncode==0 and status=='200' and 'network-fixture-ok' in p.stdout,(name,p)
    elif expected=='denied':
        assert status=='403' and 'network-fixture-ok' not in p.stdout,(name,p)
    else:
        assert p.returncode in (7,28) and status=='000',(name,p)
    results.append({'case':name,'exit_code':p.returncode,'http_status':status})
probe('allowed-standard-port','http://api.allowed.test/','allowed')
probe('allowed-gateway-4000','http://api.allowed.test:4000/','allowed')
probe('denied-source-port-80','http://source.denied.test/','denied')
probe('denied-source-port-4000','http://source.denied.test:4000/','denied')
direct='http://'+os.environ['TARGET_IP']+':4000/'
probe('curl-noproxy-star',direct,'blocked',('--noproxy','*'))
probe('cleared-proxy-env',direct,'blocked',cleared=True)
os.environ['NO_PROXY']='*';os.environ['no_proxy']='*'
probe('NO_PROXY-star',direct,'blocked')
try:
    with socket.create_connection((os.environ['TARGET_IP'],4000),timeout=2):
        raise AssertionError('raw TCP escaped the internal network')
except OSError:
    results.append({'case':'direct-tcp-ip','blocked':True})
p=subprocess.run(['git','-c','http.proxy=','-c','https.proxy=','ls-remote',direct+'repo.git','HEAD'],
                 capture_output=True,text=True,timeout=7)
assert p.returncode!=0 and ('Failed to connect' in p.stderr or 'Network is unreachable' in p.stderr),p
results.append({'case':'git-empty-proxy','exit_code':p.returncode})
print(json.dumps(results))
"""


def docker(*args: str, check: bool = True) -> str:
    result = subprocess.run(["docker", *args], check=check, capture_output=True, text=True, timeout=30)
    return result.stdout.strip()


@unittest.skipUnless(os.environ.get("SCI_BENCH_NETWORK_TEST_IMAGE"), "set SCI_BENCH_NETWORK_TEST_IMAGE to a locally pulled task environment image")
class NetworkDockerTests(unittest.TestCase):
    def test_gateway_and_proxy_bypasses(self):
        image = os.environ["SCI_BENCH_NETWORK_TEST_IMAGE"]
        stamp = "science-network-regression-" + uuid.uuid4().hex[:10]
        fixture = stamp + "-fixture"
        with tempfile.TemporaryDirectory(prefix="science-network-regression-") as directory:
            root = Path(directory)
            environment_dir = root / "environment"
            environment_dir.mkdir()
            (environment_dir / "Dockerfile").write_text("FROM " + image + "\n")
            trial = root / "trial"
            for name in ("agent", "verifier", "artifacts"):
                (trial / name).mkdir(parents=True)
            env = ScienceBenchDocker(
                environment_dir=environment_dir,
                environment_name=stamp,
                session_id=stamp,
                trial_paths=TrialPaths(trial_dir=trial),
                task_env_config=EnvironmentConfig(docker_image=image, allow_internet=False),
                network_allowlist=NetworkAllowlist(domains=["api.allowed.test"]),
                inference_urls=["http://api.allowed.test:4000"],
            )

            async def exercise():
                try:
                    await env.start(False)
                    proxy_id = (await env._run_docker_compose_command(["ps", "--quiet", "pier-egress-proxy"])).stdout.strip()
                    proxy = json.loads(docker("inspect", proxy_id))[0]
                    egress = next(name for name in proxy["NetworkSettings"]["Networks"] if name.endswith("_default"))
                    docker("run", "-d", "--rm", "--pull=never", "--name", fixture,
                           "--network", egress, "--network-alias", "api.allowed.test",
                           "--network-alias", "source.denied.test", image, "python3", "-u", "-c", SERVER)
                    target = json.loads(docker("inspect", fixture))[0]["NetworkSettings"]["Networks"][egress]["IPAddress"]
                    for _ in range(30):
                        control = subprocess.run(["docker", "exec", fixture, "curl", "-sS", "http://127.0.0.1:4000/"], capture_output=True, timeout=5)
                        if control.returncode == 0:
                            break
                        await asyncio.sleep(0.2)
                    else:
                        self.fail("Local network fixture did not become ready")
                    control = docker("exec", proxy_id, "bash", "-c", "exec 3<>/dev/tcp/api.allowed.test/4000; printf 'GET / HTTP/1.0\\r\\n\\r\\n' >&3; cat <&3")
                    self.assertIn("network-fixture-ok", control)
                    result = await env.exec("python3 -c " + __import__("shlex").quote(PROBES),
                                            env=env.agent_process_env({"TARGET_IP": target}), timeout_sec=60)
                    self.assertEqual(result.return_code, 0, (result.stdout, result.stderr))
                    checks = json.loads(result.stdout)
                    self.assertEqual(len(checks), 9)
                    print(json.dumps({"network_regression": checks}), flush=True)
                finally:
                    docker("rm", "-f", fixture, check=False)
                    await env.stop(False)
            asyncio.run(exercise())


if __name__ == "__main__":
    unittest.main()
