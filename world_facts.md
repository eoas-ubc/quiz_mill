---
jupytext:
  formats: ipynb,md:myst
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

In this notebook we plot the world population and the gross domestic product per country

```{code-cell} ipython3
:tags: [parameters]

year = 2000
```

```{code-cell} ipython3
from plots import sundial_plot
```

## World Population

```{code-cell} ipython3
sundial_plot('SP.POP.TOTL', 'World Population', year)
```

## Gross Domestic Product (current USD)

```{code-cell} ipython3
sundial_plot('NY.GDP.MKTP.CD', 'Gross Domestic Product', year)
```
