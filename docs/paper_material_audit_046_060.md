# Paper and bundled-material audit: tasks 046-060

Audit date: 2026-08-16

Scope: article text, article source packages, figures, supplementary/project
documentation, scientific fixtures, and the license notices needed to
redistribute those materials. This is a release audit, not legal advice.

## Decision rules

- A DOI, an arXiv download, a PubMed/PMC page, or an "open access" label is not
  by itself a third-party redistribution license.
- `--allow-restricted-licenses` is only a selection gate. It does not create a
  copyright license and cannot make rights-unclear paper assets distributable.
- A citation or an independently written scientific summary is not treated as
  a redistributed copy of the cited article.
- CC BY material may be redistributed commercially when creator, title,
  source, license/link, and material changes are identified.
- Separately licensed third-party figures retain their own terms even when
  embedded in a CC-licensed article.

## Executive result

| Task | Release decision | Main reason |
| --- | --- | --- |
| 046 | BLOCK | Two complete arXiv article packages have no third-party redistribution license |
| 047 | FIX NOTICE | NIST article is redistributable, but OCR/localization attribution is incomplete |
| 048 | FIX METADATA | CC BY 4.0 article is adequately licensed; source provenance fields are empty |
| 049 | FIX NOTICE | Complete JOSS article is CC BY 4.0 but lacks local attribution/license notice |
| 050 | FIX NOTICE/METADATA | JOSS article is CC BY 4.0; notice and source commit are missing |
| 051 | PASS | Restricted article is cited, not copied; bundled manuals are BSD-licensed |
| 052 | FIX NOTICE | IEEE paper is cited, not copied; NIST documentation is redistributable with notice |
| 053 | FIX LICENSE | Paper is only summarized; bundled Apache source lacks the full LICENSE text |
| 054 | FIX NOTICE/METADATA | JOSS article is CC BY 4.0, but metadata incorrectly names a different paper |
| 055 | BLOCK | Default arXiv license does not authorize redistribution of the copied figures/article adaptation |
| 056 | BLOCK | Full CC BY paper includes an apparently unlicensed Vallado textbook figure |
| 057 | BLOCK + OPT-IN | Exact abstract copied from a non-OA article; source/manual are LGPL-2.1 |
| 058 | FIX METADATA | No article is copied; source repository and commit are omitted despite known provenance |
| 059 | PASS | Papers are cited only; exact fixture is upstream CC0 data |
| 060 | PASS | Both complete articles are CC BY 4.0; dataset terms and modifications are disclosed |

The current public/release classification is therefore not sufficient: tasks
046, 055, and 056 are currently marked unrestricted even though their bundled
paper assets block release. Task 057 is correctly gated for LGPL, but the gate
does not cure the copied abstract.

## Per-task findings

### 046 - BLOCK

Bundled material:

- Vaughan and Nowak, arXiv `astro-ph/9610257`: PDF, TeX source, EPS figure, and
  style files.
- Ingram, arXiv `1909.01385`: PDF, TeX source, bibliography, article figures,
  and a converted full-text HTML copy.
- Bachetti et al., JOSS DOI `10.21105/joss.07389`: PDF.

The two arXiv records do not use Creative Commons licenses. The 1996 record
links to arXiv's `assumed-1991-2003` terms, under which arXiv assumes that
arXiv itself has a non-exclusive distribution license. The 2019 record links
to `nonexclusive-distrib/1.0`, which grants that license to arXiv. Neither
grants this benchmark a public redistribution license. The journal DOI records
also do not supply an alternative open-content license for these versions.

The JOSS paper is CC BY 4.0 and may remain with complete attribution.

Required remediation:

1. Remove both `vaughan_nowak_1997/` and `ingram_2019/` from every public task
   payload and environment image.
2. Replace them with citations and an independently written method summary.
3. Keep the JOSS PDF, adding creator, title, DOI, CC BY 4.0 URL, copyright, and
   an unchanged/modified statement.

Primary evidence:

- <https://arxiv.org/abs/astro-ph/9610257>
- <https://arxiv.org/licenses/assumed-1991-2003/>
- <https://arxiv.org/abs/1909.01385>
- <https://arxiv.org/licenses/nonexclusive-distrib/1.0/>
- <https://api.crossref.org/works/10.21105/joss.07389>

### 047 - FIX NOTICE

The complete NIST article, an OCR Markdown conversion, and localized figures
are bundled. Both authors are identified as NIST employees in the article.
NIST's policy for its Technical Series grants worldwide rights to reprint and
prepare derivative works where NIST may assert foreign rights.

Required remediation: add the recommended NIST citation, "Republished courtesy
of the National Institute of Standards and Technology", and a dated statement
that the Markdown and extracted images are conversions of the original PDF.

Primary evidence:

- <https://doi.org/10.6028/jres.097.024>
- <https://www.nist.gov/open/copyright-fair-use-and-licensing-statements-srd-data-and-software#techpubs>

### 048 - FIX METADATA

The pycalphad JORS version of record and localized Markdown are CC BY 4.0.
The local README already records authors, DOI, publisher source, license URL,
retrieval date, hash, and the fact that the Markdown is a localization. The two
non-open CALPHAD works are cited but not copied. The benchmark-authored case
study is an original note.

Required remediation: populate `source_repository` and `source_commit`, and
aggregate the existing CC BY attribution into the release NOTICE. Do not add
the cited restricted CALPHAD articles.

Primary evidence:

- <https://api.crossref.org/works/10.5334/jors.140>
- <https://creativecommons.org/licenses/by/4.0/>

### 049 - FIX NOTICE

`paper.md` and `paper_assets/paper.bib` are byte-identical to the upstream JOSS
submission files. The published article is DOI `10.21105/joss.02158`, CC BY
4.0. The local copy currently omits the DOI, CC license/link, copyright holder,
source URL, and change statement.

Required remediation: add a local attribution header or adjacent NOTICE with
the missing fields and identify the file as an unchanged upstream submission
or describe any differences from the version of record.

Primary evidence: <https://api.crossref.org/works/10.21105/joss.02158>

### 050 - FIX NOTICE/METADATA

The complete quimb JOSS submission and its figure are bundled. DOI
`10.21105/joss.00819` is CC BY 4.0. The task-level index gives the author and
DOI but not the license, source, copyright, or modification state. The release
also has an empty `source_commit`.

Required remediation: add the CC BY attribution/change statement and recover
the exact source commit before release.

Primary evidence: <https://api.crossref.org/works/10.21105/joss.00819>

### 051 - PASS

The SHTools paper is licensed CC BY-NC-ND 4.0, but no copy of that paper is
bundled. `paper.md` contains a citation and benchmark-authored explanations.
The complete manuals are part of the BSD-3-Clause source snapshot. A citation
to a restricted work does not make the task restricted.

Primary evidence: <https://api.crossref.org/works/10.1029/2018GC007529>

### 052 - FIX NOTICE

The IEEE FiPy paper is cited but not copied. The finite-volume chapter and
phase-field example are upstream FiPy/NIST documentation covered by the
bundled NIST terms, which permit copying, modification, and distribution in
the US and abroad subject to notice and attribution.

Required remediation: retain the NIST license and add a dated modification or
unchanged-copy statement for the duplicated documentation/example files.

Primary evidence:

- <https://doi.org/10.1109/MCSE.2009.52>
- <https://www.nist.gov/open/copyright-fair-use-and-licensing-statements-srd-data-and-software>

### 053 - FIX LICENSE

The arXiv paper is cited but not copied. `paper.md` is an independently written
metric explanation and `paper_assets/` contains only a README. The MONAI source
files carry Apache-2.0 headers, but the task snapshot omits the full Apache
license text and the release metadata points only to a GitHub API lookup.

Required remediation: include the upstream Apache-2.0 LICENSE in the task and
both image layers; do not rely on an online lookup for redistributed source.

### 054 - FIX NOTICE/METADATA

Lines 1-157 of `paper.md`, its bibliography, and three figures form the JOSS
paper "matchms - processing and similarity evaluation of mass spectrometry
data", DOI `10.21105/joss.02411`, CC BY 4.0. Lines 158 onward are a
benchmark-authored entropy-method summary that only cites the two Nature
Methods papers. No Nature article or figure is bundled.

`metadata.json` incorrectly identifies the 2023 Nature paper as the sole
associated paper and fails to identify the copied JOSS work.

Required remediation: record the JOSS work as the redistributed paper with
complete CC BY attribution and an adaptation statement; list the Nature works
as citation-only method references.

Primary evidence: <https://api.crossref.org/works/10.21105/joss.02411>

### 055 - BLOCK

The arXiv page for `1705.05165` uses arXiv's non-exclusive distribution
license, not a Creative Commons license. The task bundles three original paper
figures and a long Markdown adaptation presented as an offline transcription.
The arXiv license grants distribution rights to arXiv, not to this benchmark.

Required remediation: remove all three figures and replace `paper.md` with an
independently written method summary plus citation/link. An explicit user gate
cannot cure the absent redistribution license.

Primary evidence:

- <https://arxiv.org/abs/1705.05165>
- <https://arxiv.org/licenses/nonexclusive-distrib/1.0/>

### 056 - BLOCK

The task bundles a converted copy of the full SciPy 2022 proceedings paper and
all upstream figures. SciPy's 2022 publication metadata identifies proceedings
articles as CC BY 3.0, so the article and author-created figures can be
redistributed with attribution and a conversion notice.

Two embedded figures require separate handling:

- `enckes_method.pdf` is attributed only as "Wikipedia, CC BY-SA 3.0". The
  likely Wikimedia source is `File:Enckes method-vector.svg`, credited to
  GregorDS and currently identified as CC BY-SA 4.0. The local notice lacks the
  creator, source page, exact license URL, and SVG-to-PDF conversion statement.
- `leo-perturbations.png` is attributed only to Vallado's 2007 commercial
  textbook. No redistribution license or permission is bundled or found. The
  proceedings-wide CC BY license does not relicense a third-party textbook
  figure.

The local conversion also omits `refs.bib`, leaving citation keys unresolved,
so it is not a complete usable offline paper package.

Required remediation:

1. Remove `leo-perturbations.png` and its embedded reference, or obtain written
   permission/a valid open-license source.
2. Add complete Wikimedia attribution for `enckes_method.pdf` or remove it.
3. Add the SciPy CC BY 3.0 attribution and Markdown conversion statement.
4. Add the upstream bibliography or render complete references.

Primary evidence:

- <https://github.com/scipy-conference/scipy_proceedings/blob/2022/scipy_proc.json>
- <https://github.com/scipy-conference/scipy_proceedings/tree/2022/papers/juanluis_cano_poliastro>
- <https://commons.wikimedia.org/wiki/File:Enckes_method-vector.svg>

### 057 - BLOCK + OPT-IN

The source and complete manual are LGPL-2.1 and are correctly classified as a
restricted-license task requiring `--allow-restricted-licenses`.

Separately, `paper.md` reproduces the complete journal abstract verbatim. The
PMC OA API returns `idIsNotOpenAccess` for PMC4623899, and the Crossref record
does not supply a Creative Commons license. The presence of a PMC page does not
authorize republication of the abstract.

Required remediation: replace the quoted abstract with an independently
written summary. Keep the LGPL gate and all LGPL source/distribution notices.
The gate does not authorize the copied abstract.

Primary evidence:

- <https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC4623899>
- <https://api.crossref.org/works/10.1016/j.bpj.2015.08.015>

### 058 - FIX METADATA

No article text or figure is bundled; the Elsevier paper is cited and
summarized. The OpenMC manual and source are MIT-licensed. Internal provenance
records identify repository `https://github.com/openmc-dev/openmc` and pre-fix
commit `97e04c464a279500bc740a1151fef5c629796e89`, but both public metadata fields
are empty.

Required remediation: restore those two public provenance fields. Publishing a
source snapshot without identifying its source is not acceptable release
metadata and is unnecessary for preventing answer leakage.

### 059 - PASS

Both papers are cited and independently summarized; no paper text or figures
are copied. `fixtures/cell.png` is byte-identical to upstream
`skimage/data/cell.png` at the pinned commit. The upstream `cell()` docstring
explicitly dedicates the image to CC0/public domain and permits copying,
modification, and distribution. The task records its origin, native spacing,
and CC0 status. Source is BSD-3-Clause.

Primary evidence:

- <https://github.com/scikit-image/scikit-image/blob/e4e3ab682f0ff13460877624ecf068b9652ae071/skimage/data/_fetchers.py#L688>
- <https://doi.org/10.1364/OE.26.010729>

### 060 - PASS

Both bundled JATS packages state CC BY 4.0 in their own XML. The NCBI OA API
also reports CC BY for PMC7704107 and PMC10897502. Every non-thumbnail article
image referenced by the XML is present, and copyright statements remain in the
XML. The DREDge preprint is cited but not copied.

The real recording fixture is separately documented as ODbL 1.0 at the
database level and CC BY-SA 4.0 for individual contents. The README attributes
the provider, gives the source repository/commit/path, states the exact binary
copies, and describes the CRLF-to-LF metadata transformation. These licenses
permit commercial redistribution; they impose attribution/share-alike duties
but are not non-commercial licenses.

Primary evidence:

- <https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC7704107>
- <https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC10897502>
- <https://creativecommons.org/licenses/by/4.0/>
- <https://opendatacommons.org/licenses/odbl/1-0/>
- <https://creativecommons.org/licenses/by-sa/4.0/>

## Release-impact summary

Before rebuilding/publishing these images:

1. Remove or replace rights-unclear assets in 046, 055, 056, and the copied
   abstract in 057.
2. Add attribution/changes notices for 047, 049, 050, 052, 054, and 056.
3. Add the full Apache-2.0 license to 053.
4. Correct missing/mismatched provenance in 048, 050, 054, and 058.
5. Rebuild affected environment images and update their digests; verifier
   images only need rebuilding if they also contain the public task corpus.
6. Re-run the release validator with a rule that scans every task payload for
   paper assets and requires per-asset provenance/license classifications.

## Remediation record

The remediation described above was completed on 2026-08-16 in the release
workspace. The public task payloads now exclude the identified rights-unclear
assets and the copied abstract, while retaining the required attribution,
source, modification, and restricted-license notices. The affected
environment and verifier images were rebuilt as `linux/amd64` images and
published to Docker Hub with immutable `v0.1.1` references. The final image
references and material-manifest hashes are recorded in
`manifests/tasks.jsonl`; the build digest ledger is retained in the local
release build records.

Published remediation set: `046`, `047`, `048`, `049`, `050`, `052`, `053`,
`054`, `055`, `056`, `057`, `058`.
