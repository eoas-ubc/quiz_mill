---
jupytext:
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

# Remove Quizzes
Script to remove all Two Layers quizzes from Canvas.

## Running the script

```{code-cell} ipython3
%%bash
python ../quiz_mill/remove_quizzes.py
```

## How the script works

### Import libraries

```{code-cell} ipython3
from canvasapi import Canvas
from pathlib import Path
import yaml
```

### Set variables
#### Decide whether to print out statements

```{code-cell} ipython3
verbose = True
```

#### Get tokens

```{code-cell} ipython3
path_to_token = Path('../token.yaml').absolute()
file = open(path_to_token)
token = yaml.load(file, Loader=yaml.FullLoader)
```

#### Get Canvas object

```{code-cell} ipython3
API_URL = "https://canvas.ubc.ca/"
API_KEY = token

canvas = Canvas(API_URL, token)
```

#### Get course object and assignments

```{code-cell} ipython3
COURSE_NUM = 51824
course = canvas.get_course(COURSE_NUM)
assignments = course.get_assignments()
```

### Delete Two Layers quizzes from Canvas

```{code-cell} ipython3
quizzes_to_delete = []
for assignment in assignments:
    if 'Two Layers' in str(assignment):
        assignment.delete()
        if verbose:
            print(str(assignment), "deleted")
```
