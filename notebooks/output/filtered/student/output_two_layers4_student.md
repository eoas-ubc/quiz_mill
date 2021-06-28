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
  duration: 1.398483
  end_time: '2021-06-28T20:18:30.257677'
  environment_variables: {}
  exception: null
  input_path: notebooks/two_layers.ipynb
  output_path: notebooks/output/unfiltered/output_two_layers4.ipynb
  parameters:
    albedo: 0.54
    epsilon1: 0.74
    epsilon2: 0.74
    sol: 473.2
  start_time: '2021-06-28T20:18:28.859194'
  version: 2.3.3
---

+++ {"papermill": {"duration": 0.006561, "end_time": "2021-06-28T20:18:29.702468", "exception": false, "start_time": "2021-06-28T20:18:29.695907", "status": "completed"}, "tags": []}

# getting started

in the quiz_mill folder, do:

`pip install -e . -U`


to install the quiz_mill package

Then at the command line, create a new notebook with:

`papermill -p sol 330 -p epsilon1 0.4 -p epsilon2 0.6 notebooks/two_layers.ipynb trial1.ipynb`

```{code-cell} ipython3
---
papermill:
  duration: 0.152833
  end_time: '2021-06-28T20:18:29.861234'
  exception: false
  start_time: '2021-06-28T20:18:29.708401'
  status: completed
tags: []
---
from quiz_mill.solve_layers import do_two, do_two_matrix, find_temps
```

```{code-cell} ipython3
---
papermill:
  duration: 0.010541
  end_time: '2021-06-28T20:18:29.896520'
  exception: false
  start_time: '2021-06-28T20:18:29.885979'
  status: completed
tags: [injected-parameters]
---
# Parameters
sol = 473.2
epsilon1 = 0.74
epsilon2 = 0.74
albedo = 0.54
```

+++ {"quesnum": "1", "ctype": "question"}

q1: Given the above parameters, find the temperature of layer 1.
