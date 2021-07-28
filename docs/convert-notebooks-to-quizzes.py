# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Convert Jupyter notebooks to Canvas quizzes
# This guide shows you how you go from Jupyter notebooks to generating multiple quizzes and sending them to Canvas. The following steps allow you to run the commands in the notebook (on a JupyterHub), but simply copy and paste the commands in your terminal if running on your local machine.
# ***
# ### Prerequisites:
# - Must have the Canvas API token
# - Must have the base notebook
#
# ### Step 1: Remove any old "Two Layers" quizzes from Canvas (if applicable)
# Run the following cell:

# %% language="bash"
# remove-quizzes ../token.yaml -v

# %% [markdown]
# ### Step 2: Remove any old notebooks from `output/` folder (if applicable)

# %% language="bash"
# clean-output -v

# %% [markdown]
# ### Step 3: Generate **n** notebooks with random parameters

# %% language="bash"
# NUM=5
# generate-notebooks ../notebooks -n $NUM

# %% [markdown]
# ### Step 4: Filter notebooks into student and solution notebook versions

# %% language="bash"
# filter-notebook ../notebooks/output/unfiltered ../notebooks/output/filtered

# %% [markdown]
# ### Step 5: Send solution notebooks as quizzes to Canvas

# %% language="bash"
# to-canvas ../notebooks/output/filtered/solution/ -i 51824 -v  

# %% [markdown]
# See the [reference](reference.ipynb) guide for full details of commands and options.
