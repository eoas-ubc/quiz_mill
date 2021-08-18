---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst,ipynb,py:percent
  notebook_metadata_filter: all,-language_info,-toc,-latex_envs
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# getting started

in the quiz_mill folder, do:

`pip install -e . -U`


to install the quiz_mill package

Then at the command line, create a new notebook with:

`papermill -p sol 330 -p epsilon1 0.4 -p epsilon2 0.6 notebooks/two_layers.ipynb trial1.ipynb`

```{code-cell} ipython3
from quiz_mill.solve_layers import do_two, do_two_matrix, find_temps
```

```{code-cell} ipython3
:tags: [parameters]

# Default parameters
sol = 341.0
epsilon1 = 0.55
epsilon2 = 0.55
albedo = 0.3
```

## compare the two functions

```{code-cell} ipython3
analytic_fluxes = do_two(sol, epsilon1, albedo)
numeric_fluxes = do_two_matrix(sol, albedo, epsilon1, epsilon2)
print(f"analytic temperatures: {find_temps(analytic_fluxes)}")
print(f"numeric temperatues: {find_temps(numeric_fluxes)}")
```

```{code-cell} ipython3

```
