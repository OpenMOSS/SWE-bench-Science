# Spectral resampling: independent method overview

This task concerns conservative resampling of spectral flux densities and
their uncertainties. It cites the following publication for scientific
background:

A. C. Carnall, "SpectRes: A Fast Spectral Resampling Tool in Python" (2017),
arXiv `1705.05165`, <https://arxiv.org/abs/1705.05165>.

The article and its figures are **not redistributed** in this task. The arXiv
record uses arXiv's default submission terms rather than a content license
that permits this dataset to republish the paper. The explanation below is an
independently written account of the general numerical method.

## Bins, edges, and overlap

A sampled flux density represents an average over a finite coordinate
interval, not a value that can be moved to a new center without considering
bin width. For sorted centers `x[i]`, interior edges can be placed halfway
between adjacent centers. Endpoint edges must be extrapolated using the local
half-spacing. This construction works for nonuniform as well as uniform
grids, provided the centers are strictly ordered and each resulting width is
positive.

For an input bin `i` and output bin `j`, define the overlap length

```text
overlap[i,j] = max(0, min(input_upper[i], output_upper[j])
                       - max(input_lower[i], output_lower[j])).
```

When an output interval has covered width `W[j]`, its flux density is the
overlap-weighted average

```text
output_flux[j] = sum_i(overlap[i,j] * input_flux[i]) / W[j].
```

This preserves integrated flux over the covered interval. A workflow should
define explicitly what happens when an output bin is partly or wholly outside
the input coverage instead of silently treating missing width as measured
zero flux.

## Uncertainty and covariance

For independent input standard deviations `sigma[i]`, the variance of an
overlap-weighted result is

```text
output_variance[j] =
    sum_i(overlap[i,j]^2 * sigma[i]^2) / W[j]^2.
```

Thus weights are squared when propagating variance. Code that stores variance,
standard deviation, or inverse variance must convert at a clear representation
boundary. Applying a standard-deviation formula directly to variance values,
or taking a reciprocal in the middle of the weighted sum, changes the physical
meaning of the output.

Two output bins that share an input bin are generally correlated even if the
inputs were independent. Their covariance is the sum of the products of their
normalized overlap weights times the corresponding input variances. A returned
one-dimensional uncertainty array reports marginal errors only; it does not
imply independence between neighboring resampled bins.

In model-to-observation comparisons it is often preferable to resample the
model onto the observed grid. That leaves the observed noise model untouched
and avoids manufacturing additional covariance in the measured data. The
historical source snapshot and its normal documentation under
`/opt/swebench/source` provide the implementation context for this task.

