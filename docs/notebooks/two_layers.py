# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: md:myst,ipynb,py:percent
#     notebook_metadata_filter: all,-language_info,-toc,-latex_envs
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
# # getting started
#
# in the quiz_mill folder, do:
#
# `pip install -e . -U`
#
#
# to install the quiz_mill package
#
# Then at the command line, create a new notebook with:
#
# `papermill -p sol 330 -p epsilon1 0.4 -p epsilon2 0.6 notebooks/two_layers.ipynb trial1.ipynb`
#

# %%
from quiz_mill.solve_layers import do_two, do_two_matrix, find_temps

# %%
# Default parameters
sol = 341.0
epsilon1 = 0.55
epsilon2 = 0.55
albedo = 0.3

# %% [markdown]
# ## compare the two functions

# %%
analytic_fluxes = do_two(sol, epsilon1, albedo)
numeric_fluxes = do_two_matrix(sol, albedo, epsilon1, epsilon2)
print(f"analytic temperatures: {find_temps(analytic_fluxes)}")
print(f"numeric temperatues: {find_temps(numeric_fluxes)}")

# %%
