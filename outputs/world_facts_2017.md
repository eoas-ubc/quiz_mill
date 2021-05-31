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
papermill:
  duration: 4.981095
  end_time: '2019-09-24T09:49:26.073353'
  environment_variables: {}
  exception: null
  input_path: world_facts.ipynb
  output_path: world_facts_2017.ipynb
  parameters:
    year: 2017
  start_time: '2019-09-24T09:49:21.092258'
  version: 1.2.0
---

+++ {"papermill": {"duration": 0.010925, "end_time": "2019-09-24T09:49:21.794239", "exception": false, "start_time": "2019-09-24T09:49:21.783314", "status": "completed"}, "tags": []}

In this notebook we plot the world population and the gross domestic product per country

```{code-cell} ipython3
---
papermill:
  duration: 0.020995
  end_time: '2019-09-24T09:49:21.849334'
  exception: false
  start_time: '2019-09-24T09:49:21.828339'
  status: completed
tags: [parameters]
---
year = 2000
```

```{code-cell} ipython3
---
papermill:
  duration: 0.013179
  end_time: '2019-09-24T09:49:21.866509'
  exception: false
  start_time: '2019-09-24T09:49:21.853330'
  status: completed
tags: [injected-parameters]
---
# Parameters
year = 2017
```

```{code-cell} ipython3
---
papermill:
  duration: 1.232749
  end_time: '2019-09-24T09:49:23.102994'
  exception: false
  start_time: '2019-09-24T09:49:21.870245'
  status: completed
tags: []
---
from plots import sundial_plot
```

+++ {"papermill": {"duration": 0.04115, "end_time": "2019-09-24T09:49:23.147805", "exception": false, "start_time": "2019-09-24T09:49:23.106655", "status": "completed"}, "tags": []}

## World Population

```{code-cell} ipython3
---
papermill:
  duration: 1.66921
  end_time: '2019-09-24T09:49:24.825874'
  exception: false
  start_time: '2019-09-24T09:49:23.156664'
  status: completed
tags: []
---
sundial_plot('SP.POP.TOTL', 'World Population', year)
```

+++ {"papermill": {"duration": 0.065791, "end_time": "2019-09-24T09:49:24.957787", "exception": false, "start_time": "2019-09-24T09:49:24.891996", "status": "completed"}, "tags": []}

## Gross Domestic Product (current USD)

```{code-cell} ipython3
---
papermill:
  duration: 0.457098
  end_time: '2019-09-24T09:49:25.475339'
  exception: false
  start_time: '2019-09-24T09:49:25.018241'
  status: completed
tags: []
---
sundial_plot('NY.GDP.MKTP.CD', 'Gross Domestic Product', year)
```
