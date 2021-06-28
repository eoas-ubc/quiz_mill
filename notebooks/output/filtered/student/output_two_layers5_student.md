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
  duration: 1.336477
  end_time: '2021-06-28T20:18:31.613976'
  environment_variables: {}
  exception: null
  input_path: notebooks/two_layers.ipynb
  output_path: notebooks/output/unfiltered/output_two_layers5.ipynb
  parameters:
    albedo: 0.69
    epsilon1: 0.28
    epsilon2: 0.28
    sol: 359.7
  start_time: '2021-06-28T20:18:30.277499'
  version: 2.3.3
---

+++ {"papermill": {"duration": 0.006407, "end_time": "2021-06-28T20:18:31.046667", "exception": false, "start_time": "2021-06-28T20:18:31.040260", "status": "completed"}, "tags": []}

# getting started

in the quiz_mill folder, do:

`pip install -e . -U`


to install the quiz_mill package

Then at the command line, create a new notebook with:

`papermill -p sol 330 -p epsilon1 0.4 -p epsilon2 0.6 notebooks/two_layers.ipynb trial1.ipynb`

```{code-cell} ipython3
---
papermill:
  duration: 0.155855
  end_time: '2021-06-28T20:18:31.208678'
  exception: false
  start_time: '2021-06-28T20:18:31.052823'
  status: completed
tags: []
---
from quiz_mill.solve_layers import do_two, do_two_matrix, find_temps
```

```{code-cell} ipython3
---
papermill:
  duration: 0.010484
  end_time: '2021-06-28T20:18:31.249710'
  exception: false
  start_time: '2021-06-28T20:18:31.239226'
  status: completed
tags: [injected-parameters]
---
# Parameters
sol = 359.7
epsilon1 = 0.28
epsilon2 = 0.28
albedo = 0.69
```

+++ {"quesnum": "1", "ctype": "question"}

q1: Given the above parameters, find the temperature of layer 1.
