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
  duration: 1.526306
  end_time: '2021-06-28T20:18:27.459462'
  environment_variables: {}
  exception: null
  input_path: notebooks/two_layers.ipynb
  output_path: notebooks/output/unfiltered/output_two_layers2.ipynb
  parameters:
    albedo: 0.63
    epsilon1: 0.62
    epsilon2: 0.62
    sol: 265.5
  start_time: '2021-06-28T20:18:25.933156'
  version: 2.3.3
---

+++ {"papermill": {"duration": 0.007028, "end_time": "2021-06-28T20:18:26.895834", "exception": false, "start_time": "2021-06-28T20:18:26.888806", "status": "completed"}, "tags": []}

# getting started

in the quiz_mill folder, do:

`pip install -e . -U`


to install the quiz_mill package

Then at the command line, create a new notebook with:

`papermill -p sol 330 -p epsilon1 0.4 -p epsilon2 0.6 notebooks/two_layers.ipynb trial1.ipynb`

```{code-cell} ipython3
---
papermill:
  duration: 0.150857
  end_time: '2021-06-28T20:18:27.052399'
  exception: false
  start_time: '2021-06-28T20:18:26.901542'
  status: completed
tags: []
---
from quiz_mill.solve_layers import do_two, do_two_matrix, find_temps
```

```{code-cell} ipython3
---
papermill:
  duration: 0.013599
  end_time: '2021-06-28T20:18:27.090152'
  exception: false
  start_time: '2021-06-28T20:18:27.076553'
  status: completed
tags: [injected-parameters]
---
# Parameters
sol = 265.5
epsilon1 = 0.62
epsilon2 = 0.62
albedo = 0.63
```

+++ {"quesnum": "1", "ctype": "question"}

q1: Given the above parameters, find the temperature of layer 1.
