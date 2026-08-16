#!/usr/bin/env python3
"""Serialize a local Docker image upload through the Docker Registry API."""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import subprocess
import tarfile
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

REGISTRY = "https://registry-1.docker.io"


def http(url: str, *, method: str = "GET", headers: dict[str, str] | None = None,
         data=None) -> tuple[int, dict[str, str], bytes]:
    request = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(request, timeout=1800) as response:
            return response.status, dict(response.headers), response.read()
    except urllib.error.HTTPError as exc:
        return exc.code, dict(exc.headers), exc.read()


def token(repository: str, mount_from: tuple[str, ...] = ()) -> str:
    result = subprocess.run(
        ["docker-credential-desktop", "get"],
        input=b"https://index.docker.io/v1/\n",
        stdout=subprocess.PIPE,
        check=True,
    )
    credentials = json.loads(result.stdout)
    basic = base64.b64encode(
        f"{credentials['Username']}:{credentials['Secret']}".encode()
    ).decode()
    query_items = [
        ("service", "registry.docker.io"),
        ("scope", f"repository:{repository}:pull,push"),
    ]
    query_items.extend(("scope", f"repository:{source}:pull") for source in mount_from)
    query = urllib.parse.urlencode(query_items)
    status, _, body = http(
        f"https://auth.docker.io/token?{query}",
        headers={"Authorization": f"Basic {basic}"},
    )
    if status != 200:
        raise RuntimeError(f"Docker Hub token request failed ({status}): {body[:300]!r}")
    return str(json.loads(body)["token"])


def digest(path: Path) -> tuple[str, int]:
    hasher = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        while chunk := stream.read(1024 * 1024):
            hasher.update(chunk)
            size += len(chunk)
    return f"sha256:{hasher.hexdigest()}", size


def upload_blob(
    repository: str,
    bearer: str,
    path: Path,
    mount_from: tuple[str, ...] = (),
) -> tuple[str, int]:
    blob_digest, size = digest(path)
    auth = {"Authorization": f"Bearer {bearer}"}
    status, _, _ = http(
        f"{REGISTRY}/v2/{repository}/blobs/{blob_digest}",
        method="HEAD",
        headers=auth,
    )
    if status == 200:
        print(f"  exists {blob_digest} ({size} bytes)", flush=True)
        return blob_digest, size
    if status not in (404, 405):
        raise RuntimeError(f"blob HEAD failed ({status}) for {blob_digest}")
    location = None
    for source in mount_from:
        mount_query = urllib.parse.urlencode({"mount": blob_digest, "from": source})
        mount_status, mount_headers, mount_body = http(
            f"{REGISTRY}/v2/{repository}/blobs/uploads/?{mount_query}",
            method="POST",
            headers=auth,
        )
        if mount_status == 201:
            print(f"  mounted {blob_digest} from {source} ({size} bytes)", flush=True)
            return blob_digest, size
        if mount_status == 202:
            location = mount_headers.get("Location") or mount_headers.get("location")
            break
        if mount_status not in (404, 405):
            print(f"  mount probe failed ({mount_status}): {mount_body[:160]!r}", flush=True)
    if location is None:
        status, headers, body = http(
            f"{REGISTRY}/v2/{repository}/blobs/uploads/",
            method="POST",
            headers=auth,
        )
    else:
        status, headers, body = 202, {"Location": location}, b""
    if status != 202:
        raise RuntimeError(f"blob upload start failed ({status}): {body[:300]!r}")
    location = headers.get("Location") or headers.get("location")
    if not location:
        raise RuntimeError("registry did not return an upload location")
    if location.startswith("/"):
        location = REGISTRY + location
    location += ("&" if "?" in location else "?") + urllib.parse.urlencode({"digest": blob_digest})
    with path.open("rb") as stream:
        request = urllib.request.Request(
            location,
            data=stream,
            headers={**auth, "Content-Type": "application/octet-stream", "Content-Length": str(size)},
            method="PUT",
        )
        try:
            with urllib.request.urlopen(request, timeout=1800) as response:
                response.read()
                status = response.status
        except urllib.error.HTTPError as exc:
            raise RuntimeError(f"blob upload failed ({exc.code}): {exc.read()[:500]!r}") from exc
    if status not in (201, 202):
        raise RuntimeError(f"blob upload returned unexpected status {status}")
    print(f"  uploaded {blob_digest} ({size} bytes)", flush=True)
    return blob_digest, size


def publish(image: str, repository: str, tag: str, mount_from: tuple[str, ...] = ()) -> str:
    bearer = token(repository, mount_from)

    def upload_with_refresh(path: Path) -> tuple[str, int]:
        nonlocal bearer
        for attempt in range(3):
            try:
                return upload_blob(repository, bearer, path, mount_from)
            except RuntimeError as exc:
                if "blob HEAD failed (401)" not in str(exc) or attempt == 2:
                    raise
                print("  registry token expired; refreshing", flush=True)
                bearer = token(repository, mount_from)
        raise AssertionError("unreachable")

    with tempfile.TemporaryDirectory(prefix="science-docker-save-") as directory:
        archive = Path(directory) / "image.tar"
        subprocess.run(["docker", "save", "-o", str(archive), image], check=True)
        with tarfile.open(archive) as bundle:
            saved = json.loads(bundle.extractfile("manifest.json").read())[0]
            names = [str(saved["Config"]), *(str(item) for item in saved["Layers"])]
            files = {}
            for name in names:
                destination = Path(directory) / name.replace("/", "_")
                with bundle.extractfile(name) as source, destination.open("wb") as target:
                    while chunk := source.read(1024 * 1024):
                        target.write(chunk)
                files[name] = destination
        config_digest, config_size = upload_with_refresh(files[str(saved["Config"])])
        layers = []
        for name in saved["Layers"]:
            layer_digest, layer_size = upload_with_refresh(files[str(name)])
            layers.append({
                "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
                "size": layer_size,
                "digest": layer_digest,
            })
        document = {
            "schemaVersion": 2,
            "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
            "config": {
                "mediaType": "application/vnd.docker.container.image.v1+json",
                "size": config_size,
                "digest": config_digest,
            },
            "layers": layers,
        }
        body = json.dumps(document, separators=(",", ":")).encode()
        status, _, response = http(
            f"{REGISTRY}/v2/{repository}/manifests/{urllib.parse.quote(tag)}",
            method="PUT",
            headers={"Authorization": f"Bearer {bearer}",
                     "Content-Type": "application/vnd.docker.distribution.manifest.v2+json"},
            data=body,
        )
        if status not in (200, 201):
            raise RuntimeError(f"manifest upload failed ({status}): {response[:500]!r}")
        manifest_digest = f"sha256:{hashlib.sha256(body).hexdigest()}"
        print(f"published {repository}:{tag} {manifest_digest}", flush=True)
        return manifest_digest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--mount-from", action="append", default=[])
    args = parser.parse_args()
    publish(args.image, args.repository, args.tag, tuple(args.mount_from))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
