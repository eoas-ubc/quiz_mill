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

+++

## How the script works

### Import libraries

+++

```
from canvasapi import Canvas
from pathlib import Path
import yaml
```

+++

### Main function
How it works:
1. Get tokens
2. Get Canvas object
3. Get course object and assignments
4. Delete Two Layers quizzes from Canvas

+++

```
def main(path, verbose):

    path_to_token = Path(path).resolve()
    file = open(path_to_token / "token.yaml")
    token = yaml.load(file, Loader=yaml.FullLoader)

    API_URL = "https://canvas.ubc.ca/"
    API_KEY = token

    canvas = Canvas(API_URL, API_KEY)

    course = canvas.get_course(51824)

    assignments = course.get_assignments()

    for assignment in assignments:
        if 'Two Layers' in str(assignment):
            assignment.delete()
            if verbose:
                print(str(assignment), "deleted")
```
