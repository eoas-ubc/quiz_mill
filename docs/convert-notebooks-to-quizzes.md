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

# Convert Jupyter notebooks to Canvas quizzes
This guide shows you how you go from Jupyter notebooks to generating multiple quizzes and sending them to Canvas. The following steps allow you to run the commands in the notebook (on a JupyterHub), but simply copy and paste the commands in your terminal if running on your local machine.
***
### Prerequisites:
- Must have the Canvas API token
- Must have the base notebook

### Step 1: Remove any old "Two Layers" quizzes from Canvas (if applicable)
Run the following cell:

```{code-cell} ipython3
%%bash
remove-quizzes ../token.yaml -v
```

### Step 2: Remove any old notebooks from `output/` folder (if applicable)

```{code-cell} ipython3
%%bash
clean-output -v
```

### Step 3: Generate **n** notebooks with random parameters

```{code-cell} ipython3
%%bash
NUM=5
generate-notebooks ../notebooks -n $NUM
```

### Step 4: Filter notebooks into student and solution notebook versions

```{code-cell} ipython3
%%bash
filter-notebook ../notebooks/output/unfiltered ../notebooks/output/filtered
```

### Step 5: Send solution notebooks as quizzes to Canvas

```{code-cell} ipython3
%%bash
to-canvas ../notebooks/output/filtered/solution/ -i 51824 -v  
```

See the [reference](reference.ipynb) guide for full details of commands and options.
