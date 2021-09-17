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
papermill:
  default_parameters: {}
  duration: 2.021539
  end_time: '2021-08-16T20:50:18.705938'
  environment_variables: {}
  exception: null
  input_path: /Users/carolzhang/Projects/eoas-ubc/quiz_mill/notebooks/two_layers.ipynb
  output_path: /Users/carolzhang/Projects/eoas-ubc/quiz_mill/notebooks/output/unfiltered/output_two_layers1.ipynb
  parameters:
    albedo: 0.14
    epsilon1: 0.63
    epsilon2: 0.63
    sol: 193.5
  start_time: '2021-08-16T20:50:16.684399'
  version: 2.3.3
---

+++ {"papermill": {"duration": 0.00712, "end_time": "2021-08-16T20:50:18.195537", "exception": false, "start_time": "2021-08-16T20:50:18.188417", "status": "completed"}, "tags": []}

# getting started 

in the quiz_mill folder, do:

`pip install -e . -U`


to install the quiz_mill package

Then at the command line, create a new notebook with:

`papermill -p sol 330 -p epsilon1 0.4 -p epsilon2 0.6 notebooks/two_layers.ipynb trial1.ipynb`

```{code-cell} ipython3
---
papermill:
  duration: 0.210044
  end_time: '2021-08-16T20:50:18.411398'
  exception: false
  start_time: '2021-08-16T20:50:18.201354'
  status: completed
tags: []
---
from quiz_mill.solve_layers import do_two, do_two_matrix, find_temps
```

```{code-cell} ipython3
---
papermill:
  duration: 0.011157
  end_time: '2021-08-16T20:50:18.427987'
  exception: false
  start_time: '2021-08-16T20:50:18.416830'
  status: completed
tags: [parameters]
---
# Default parameters
sol = 341.0
epsilon1 = 0.55
epsilon2 = 0.55
albedo = 0.3
```

```{code-cell} ipython3
---
papermill:
  duration: 0.012004
  end_time: '2021-08-16T20:50:18.445102'
  exception: false
  start_time: '2021-08-16T20:50:18.433098'
  status: completed
tags: [injected-parameters]
---
# Parameters
sol = 193.5
epsilon1 = 0.63
epsilon2 = 0.63
albedo = 0.14
```

+++ {"papermill": {"duration": 0.006085, "end_time": "2021-08-16T20:50:18.456391", "exception": false, "start_time": "2021-08-16T20:50:18.450306", "status": "completed"}, "tags": []}

## compare the two functions

```{code-cell} ipython3
---
papermill:
  duration: 0.014815
  end_time: '2021-08-16T20:50:18.476866'
  exception: false
  start_time: '2021-08-16T20:50:18.462051'
  status: completed
tags: []
---
analytic_fluxes = do_two(sol, epsilon1, albedo)
numeric_fluxes = do_two_matrix(sol, albedo, epsilon1, epsilon2)
print(f"analytic temperatures: {find_temps(analytic_fluxes)}")
print(f"numeric temperatues: {find_temps(numeric_fluxes)}")
```

```{code-cell} ipython3
---
papermill:
  duration: 0.005636
  end_time: '2021-08-16T20:50:18.490012'
  exception: false
  start_time: '2021-08-16T20:50:18.484376'
  status: completed
tags: []
---

```
