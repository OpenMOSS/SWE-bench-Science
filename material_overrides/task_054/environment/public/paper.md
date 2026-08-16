---
title: matchms - processing and similarity evaluation of mass spectrometry data.
tags:
  - Python
  - mass spectrometry
  - metadata cleaning
  - data processing
  - similarity measures
  - metabolomics

authors:
  - name: Florian Huber
    orcid: 0000-0002-3535-9406
    affiliation: 1
  - name: Stefan Verhoeven
    orcid: 0000-0002-5821-2060
    affiliation: 1
  - name: Christiaan Meijer
    orcid: 0000-0002-5529-5761
    affiliation: 1
  - name: Hanno Spreeuw
    orcid: 0000-0002-5057-0322
    affiliation: 1
  - name: Efraín Manuel Villanueva Castilla
    orcid: 0000-0001-7665-3575
    affiliation: 2
  - name: Cunliang Geng
    orcid: 0000-0002-1409-8358
    affiliation: 1
  - name: Justin J. J. van der Hooft
    orcid: 0000-0002-9340-5511
    affiliation: 3
  - name: Simon Rogers
    orcid: 0000-0003-3578-4477
    affiliation: 2
  - name: Adam Belloum
    orcid: 0000-0001-6306-6937
    affiliation: 1
  - name: Faruk Diblen
    orcid: 0000-0002-0989-929X
    affiliation: 1
  - name: Jurriaan H. Spaaks
    orcid: 0000-0002-7064-4069
    affiliation: 1

affiliations:
 - name: Netherlands eScience Center, Science Park 140, 1098XG Amsterdam, The Netherlands
   index: 1
 - name: School of Computing Science, University of Glasgow, Glasgow, United Kingdom
   index: 2
 - name: Bioinformatics Group, Plant Sciences Group, University of Wageningen, Wageningen, the Netherlands
   index: 3
date: 16 June 2020
bibliography: paper.bib

---

> **Publication attribution.** Florian Huber et al., "matchms - processing
> and similarity evaluation of mass spectrometry data," *Journal of Open
> Source Software* 5(52), 2411 (2020),
> <https://doi.org/10.21105/joss.02411>. Copyright 2020 the paper authors.
> Licensed under Creative Commons Attribution 4.0 International,
> <https://creativecommons.org/licenses/by/4.0/>. The JOSS article body and
> figures below are derived from the matchms source snapshot at commit
> `9f27ba89d8c485e6a2fa2db4756e3fe3aec05151`; the separately headed
> entropy-method overview was written for SWE-bench Science and cites, but
> does not reproduce, the two Nature Methods articles.

# Summary

Mass spectrometry data is at the heart of numerous applications in the biomedical and life sciences.
With growing use of high-throughput techniques, researchers need to analyze larger and more complex datasets. In particular through joint effort in the research community, fragmentation mass spectrometry datasets are growing in size and number.
Platforms such as MassBank [@horai_massbank_2010], GNPS [@Wang2016] or MetaboLights [@haug_metabolights_2020] serve as an open-access hub for sharing of raw, processed, or annotated fragmentation mass spectrometry data.
Without suitable tools, however, exploitation of such datasets remains overly challenging. 
In particular, large collected datasets contain data acquired using different instruments and measurement conditions, and can further contain a significant fraction of inconsistent, wrongly labeled, or incorrect metadata (annotations).

``matchms`` is an open-source Python package to import, process, clean, and compare mass spectrometry data (MS/MS) (see \autoref{fig:flowchart}).
It allows to implement and run an easy-to-follow, easy-to-reproduce workflow from raw mass spectra to pre- and post-processed spectral data. 
Raw data can be imported from the commonly used formats msp, mzML [@martens_mzmlcommunity_2011], mzXML, MGF (mzML, mzXML, MGF file importers are built on top of pyteomics [@levitsky_pyteomics_2019;@goloborodko_pyteomicspython_2013], as well as from JSON files (as provided by GNPS), but also via Universal Spectrum Identifiers (USI) [@wang_interactive_2020]. Further data formats or more extensive options regarding metadata parsing can best be handled by using pyteomics [@levitsky_pyteomics_2019] or pymzml [@kosters_pymzml_2018].
``matchms`` contains numerous metadata cleaning and harmonizing filter functions that can easily be stacked to construct a desired pipeline (\autoref{fig:filtering}), which can also easily be extended by custom functions wherever needed. Available filters include extensive cleaning, correcting, checking of key metadata fields such as compound name, structure annotations (InChI, SMILES, InChIKey), ionmode, adduct, or charge.
Many of the provided metadata cleaning filters were designed for handling and improving GNPS-style MGF or JSON datasets. For future versions, however, we aim to further extend this to other commonly used public databases.

![Flowchart of ``matchms`` workflow. Reference and query spectrums are filtered using the same set of set filters (here: filter A and filter B). Once filtered, every reference spectrum is compared to every query spectrum using the ``matchms.Scores`` object. \label{fig:flowchart}](paper_assets/flowchart_matchms.png)

Current Python tools for working with MS/MS data include pyOpenMS [@rost_pyopenms_2014], a wrapper for OpenMS [@rost_openms_2016] with a strong focus on processing and filtering of raw mass spectral data. 
pyOpenMS has a wide range of peak processing functions which can be used to further complement a ``matchms`` filtering pipeline.
Another, more lightweight and native Python package with a focus on spectra visualization is ``spectrum_utils`` [@bittremieux_spectrum_utils_2020].
``matchms`` focuses on comparing and linking large number of mass spectra. Many of its built-in filters are aimed at handling large mass spectra datasets from common public data libraries such as GNPS.

``matchms`` provides functions to derive different similarity scores between spectra. Those include the established spectra-based measures of the cosine score or modified cosine score [@watrous_mass_2012].
The package also offers fast implementations of common similarity measures (Dice, Jaccard, Cosine) that can be used to compute similarity scores between molecular fingerprints (rdkit, morgan1, morgan2, morgan3, all implemented using rdkit [@rdkit]).
``matchms`` facilitates easily deriving similarity measures between large number of spectra at comparably fast speed due to score implementations based on NumPy [@van_der_walt_numpy_2011], SciPy [@2020SciPy-NMeth], and Numba [@lam_numba_2015]. Additional similarity measures can easily be added using the ``matchms`` API. 
The provided API also allows to quickly compare, sort, and inspect query versus reference spectra using either the included similarity scores or added custom measures.
The API was designed to be easily extensible so that users can add their own filters for spectra processing, or their own similarity functions for spectral comparisons.
The present set of filters and similarity functions was mostly geared towards smaller molecules and natural compounds, but it could easily be extended by functions specific to larger peptides or proteins.

``matchms`` is freely accessible either as conda package (https://anaconda.org/nlesc/matchms), or in form of source-code on GitHub (https://github.com/matchms/matchms). For further code examples and documentation see https://matchms.readthedocs.io/en/latest/.
All main functions are covered by tests and continuous integration to offer reliable functionality.
We explicitly value future contributions from a mass spectrometry interested community and hope that ``matchms`` can serve as a reliable and accessible entry point for handling complex mass spectrometry datasets using Python. 


# Example workflow
A typical workflow with ``matchms`` looks as indicated in \autoref{fig:flowchart}, or as described in the following code example.
```python
from matchms.importing import load_from_mgf
from matchms.filtering import default_filters
from matchms.filtering import normalize_intensities
from matchms import calculate_scores
from matchms.similarity import CosineGreedy

# Read spectrums from a MGF formatted file
file = load_from_mgf("all_your_spectrums.mgf")

# Apply filters to clean and enhance each spectrum
spectrums = []
for spectrum in file:
    spectrum = default_filters(spectrum)
    spectrum = normalize_intensities(spectrum)
    spectrums.append(spectrum)

# Calculate Cosine similarity scores between all spectrums
scores = calculate_scores(references=spectrums,
                          queries=spectrums,
                          similarity_function=CosineGreedy())

# Print the calculated scores for each spectrum pair
for score in scores:
    (reference, query, score, n_matching) = score
    # Ignore scores between same spectrum and
    # pairs which have less than 20 peaks in common
    if reference is not query and n_matching >= 20:
        print(f"Reference scan id: {reference.metadata['scans']}")
        print(f"Query scan id: {query.metadata['scans']}")
        print(f"Score: {score:.4f}")
        print(f"Number of matching peaks: {n_matching}")
        print("----------------------------")
```

![``matchms`` provides a range of filter functions to process spectrum peaks and metadata. Filters can easily be stacked and combined to build a desired pipeline. The API also makes it easy to extend customer pipelines by adding own filter functions. \label{fig:filtering}](paper_assets/filtering_sketch.png)

# Processing spectrum peaks and plotting
``matchms`` provides numerous filters to process mass spectra peaks. Below a simple example to remove low intensity peaks from a spectrum (\autoref{fig:peak_filtering}).
```python
from matchms.filtering import require_minimum_number_of_peaks
from matchms.filtering import select_by_mz
from matchms.filtering import select_by_relative_intensity

def process_peaks(s):
    s = select_by_mz(s, mz_from=0, mz_to=1000)
    s = select_by_relative_intensity(s, intensity_from=0.001)
    s = require_minimum_number_of_peaks(s, n_required=10)
    return s

# Apply processing steps to spectra (here to a single "spectrum_raw")
spectrum_processed = process_peaks(spectrum_raw)

# Plot raw spectrum (all and zoomed in)
spectrum_raw.plot()
spectrum_raw.plot(intensity_to=0.02)

# Plot processed spectrum (all and zoomed in)
spectrum_processed.plot()
spectrum_processed.plot(intensity_to=0.02)
```

![Example of ``matchms`` peak filtering applied to an actual spectrum using ``select_by_relative_intensity`` to remove peaks of low relative intensity. Spectra are plotted using the provided ``spectrum.plot()`` function. \label{fig:peak_filtering}](paper_assets/peak_filtering.png)


# Scientific background for entropy-based MS/MS comparison

The task concerns a similarity measure for tandem mass spectra. A spectrum is
represented by fragment locations (mass-to-charge, or `m/z`) and measured
intensities. For a valid spectrum with non-negative intensities, the normalized
intensity of peak (i) can be written as

\[
p_i = \frac{I_i}{\sum_j I_j}.
\]

The spectral entropy is the Shannon entropy of this distribution:

\[
H(p) = -\sum_i p_i \ln p_i,
\]

with zero-probability terms contributing zero. Entropy-based similarity uses
the information carried by compatible fragment peaks in two spectra. The
result is normalized so that identical valid spectra provide the upper
reference behavior and spectra without compatible fragments do not receive a
matched-fragment contribution. The exact calculation also depends on the
chosen mass tolerance, which may be expressed in Dalton or in parts per
million.

The method papers describe spectral entropy as an alternative to conventional
dot-product scores for small-molecule MS/MS identification and describe Flash
Entropy Search as an acceleration for querying large spectral libraries:

- Li, Kind, Folz et al., “Spectral entropy outperforms MS/MS dot product
  similarity for small-molecule compound identification,” *Nature Methods*
  18, 1524–1531 (2021),
  https://doi.org/10.1038/s41592-021-01331-z
- Li and Fiehn, “Flash entropy search to query all mass spectral libraries in
  real time,” *Nature Methods* 20, 1475–1478 (2023),
  https://doi.org/10.1038/s41592-023-02012-9

For this workflow, an accelerated library query is an implementation of the
same scientific comparison, not a new similarity definition. Changing the
index or the order in which candidate spectra are visited should therefore
not change the result that a researcher obtains for a given pair of spectra.
The source tree and the offline reproduction provide the implementation
context needed to investigate the observed discrepancy.

# References
