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
## Prerequisites:
- Must have the Canvas API token
- Must have the base notebook

## Step 1: Remove any old "Two Layers" quizzes from Canvas (if applicable)
Run the following cell:

```{code-cell} ipython3
%%bash
remove -v ..
```

### Output should be similar to the following:
![remove output](output_remove_canvas.png)

+++

## Step 2: Remove any old notebooks from `output/` folder (if applicable)
Run the following cell:

```{code-cell} ipython3
%%bash
clean -v
```

### Output should be similar to the following:
![clean output](output_clean.png)

+++

## Step 3: Generate **N** notebooks with random parameters
Run the following cell:

```{code-cell} ipython3
%%bash
N=5
generate -n $N ../notebooks
```

### Expected output:
![generate notebooks expected output](output_generate.png)

### What the notebook should look like:
![unfiltered notebook](unfiltered_notebook.png)
The notebook is located at `quiz_mill/notebooks/output/unfiltered/`.

+++

## Step 4: Filter notebooks into student and solution notebook versions
Run the following cell:

```{code-cell} ipython3
%%bash
filter -v ../notebooks/output
```

### Expected output:
![filter notebook](output_filter.png)

### Student notebook:
![student notebook](student_notebook.png)

### Solution notebook:
![solution notebook](solution_notebook.png)

+++

### Step 5: Send solution notebooks as quizzes to Canvas
Run the following cell:

```{code-cell} ipython3
%%bash
send -c 51824 -v ../notebooks/output/filtered/solution/
```

### Expected output:
![to-canvas output](out_to_canvas.png)

### What you should see on Canvas:
![quizzes on Canvas](canvas_quizzes.png)

+++

See the [reference](reference.ipynb) guide for full details of commands and options.
