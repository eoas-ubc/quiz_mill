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

# Quickstart
Skip all the details and run the below code cell to generate quizzes and push them to Canvas.

+++

## Requirements
1. Canvas API token is in outermost `quiz-mill/` folder. Learn how to get the Canvas API token [here](canvas-api.ipynb).

+++

Run this code cell (assign NUM variable the desired number of quizzes):

```{code-cell} ipython3
%%bash
NUM=5
sh ../quiz_mill/do_all.sh $NUM 
```

What did the above cell do?
1. Removed all previous "Two Layers" quizzes from Canvas
2. Removed all previous notebooks in `output/` folder
3. Generate `NUM` notebooks with randomly generated parameters
4. Filter notebooks into student and solution versions
5. Push the solution version notebooks to Canvas
