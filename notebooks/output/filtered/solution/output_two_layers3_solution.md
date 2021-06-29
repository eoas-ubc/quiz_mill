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
  duration: 1.353957
  end_time: '2021-06-28T20:18:28.835832'
  environment_variables: {}
  exception: null
  input_path: notebooks/two_layers.ipynb
  output_path: notebooks/output/unfiltered/output_two_layers3.ipynb
  parameters:
    albedo: 0.46
    epsilon1: 0.31
    epsilon2: 0.31
    sol: 487.2
  start_time: '2021-06-28T20:18:27.481875'
  version: 2.3.3
---

+++ {"papermill": {"duration": 0.006181, "end_time": "2021-06-28T20:18:28.270753", "exception": false, "start_time": "2021-06-28T20:18:28.264572", "status": "completed"}, "tags": []}

# getting started

in the quiz_mill folder, do:

`pip install -e . -U`


to install the quiz_mill package

Then at the command line, create a new notebook with:

`papermill -p sol 330 -p epsilon1 0.4 -p epsilon2 0.6 notebooks/two_layers.ipynb trial1.ipynb`

```{code-cell} ipython3
---
papermill:
  duration: 0.155443
  end_time: '2021-06-28T20:18:28.434461'
  exception: false
  start_time: '2021-06-28T20:18:28.279018'
  status: completed
tags: []
---
from quiz_mill.solve_layers import do_two, do_two_matrix, find_temps
```

```{code-cell} ipython3
---
papermill:
  duration: 0.012066
  end_time: '2021-06-28T20:18:28.471449'
  exception: false
  start_time: '2021-06-28T20:18:28.459383'
  status: completed
tags: [injected-parameters]
---
# Parameters
sol = 487.2
epsilon1 = 0.31
epsilon2 = 0.31
albedo = 0.46
```

+++ {"quesnum": "1", "ctype": "question"}

q1: Given the above parameters, find the temperature of layer 1.

+++ {"quesnum": "1", "ctype": "answer"}

answer: 63.21895668639054
