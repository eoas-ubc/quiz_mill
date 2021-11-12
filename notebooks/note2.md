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
---

```{code-cell}
---
ctype: question
papermill:
  duration: 0.087468
  end_time: '2021-06-07T20:10:58.366832'
  exception: false
  start_time: '2021-06-07T20:10:58.279364'
  status: completed
quesnum: 0
tags: []
---
"""
   This notebook solves two equations in two unknowns to find the equilibrium
   radiative balance in a two layer atmosphere over a black ground surface
   
   ---------------
   abs2
   ---------------
   abs1
   ---------------
   _______________________  Fg
   
   layers.py provides two functions:
      do_two(Sol=341.,epsilon=0.55,albedo=0.3)
         -- this solves the two layer model analytically

      do_two_matrix(Sol=341.,albedo=0.3,epsilon1=0.55,epsilon2=0.55)         
          -- this solves the two layer model numerically
"""
import numpy as np
from scipy import linalg
```

+++ {"quesnum": 0, "ctype": "answer"}

q0 answer here

```{code-cell}
---
ctype: question
papermill:
  duration: 0.009625
  end_time: '2021-06-07T20:10:58.381071'
  exception: false
  start_time: '2021-06-07T20:10:58.371446'
  status: completed
quesnum: 1
tags: [parameters]
---
# Default parameters
sol = 341.0
epsilon1 = 0.55
epsilon2 = 0.55
albedo = 0.3
```

+++ {"quesnum": 1, "ctype": "answer"}

q1 answer here

```{code-cell}
---
ctype: question
papermill:
  duration: 0.007756
  end_time: '2021-06-07T20:10:58.393260'
  exception: false
  start_time: '2021-06-07T20:10:58.385504'
  status: completed
quesnum: 2
tags: []
---
def do_two(Sol=341.0, epsilon=0.55, albedo=0.3):
    """

    Calculate equlibrium fluxes for a two-layer atmosphere

     Parameters
     ----------

     Sol: float
          day/night averaged TOA shortwave flux (W/m^2)
     epsilon: float
           longwave emissivity of layers 1 and 2
     albedo: float
           shortwave reflectivity of surface

     Returns
     -------

     fluxes: tuple
        (Fg,F1,F2) -- equilibrium fluxes for ground, layer1, layer2 (W/m^2)


    """
    Fg = (
        (1 - albedo)
        * Sol
        / (
            1
            - epsilon
            / 2
            * (1 + epsilon * (1 - epsilon) / 2)
            / (1 - epsilon * epsilon / 4)
            - (1 - epsilon)
            * epsilon
            / 2
            * ((1 - epsilon) + epsilon / 2)
            / (1 - epsilon * epsilon / 4)
        )
    )
    F2 = Fg * epsilon / 2 * ((1 - epsilon) + epsilon / 2) / (1 - epsilon * epsilon / 4)
    F1 = (
        Fg
        * epsilon
        / 2
        * (1 + epsilon * (1 - epsilon) / 2)
        / (1 - epsilon * epsilon / 4)
    )
    # check balances
    TOA = Sol * (1 - albedo) - F2 - (1 - epsilon) * F1 - (1 - epsilon) ** 2.0 * Fg
    Lay1 = Sol * (1 - albedo) + F2 - F1 - (1 - epsilon) * Fg
    Ground = Sol * (1 - albedo) + F1 + (1 - epsilon) * F2 - Fg
    fluxes = (Fg, F1, F2)
    return fluxes
```

+++ {"quesnum": 2, "ctype": "answer"}

q2 answer here

```{code-cell}
---
ctype: question
papermill:
  duration: 0.006803
  end_time: '2021-06-07T20:10:58.402735'
  exception: false
  start_time: '2021-06-07T20:10:58.395932'
  status: completed
quesnum: 3
tags: []
---
def do_two_matrix(Sol=341.0, albedo=0.3, epsilon1=0.55, epsilon2=0.55):
    """
     do_two_matrix(Sol=341.,albedo=0.3,epsilon1=0.55,epsilon2=0.55)
     returns [Fg,F1,F2]   -- layer fluxes in W/m^2

    Calculate equlibrium fluxes for a two-layer atmosphere

     Parameters
     ----------

     Sol: float
          day/night averaged TOA shortwave flux (W/m^2)
     epsilon1: float
           longwave emissivity for layer 1
     epsilon2: float
           longwave emissivity for layer 2
     albedo: float
           shortwave reflectivity of surface

     Returns
     -------

     fluxes: numpy verctor
        (Fg,F1,F2) -- equilibrium fluxes for ground, layer1, layer2


    """
    Sol = Sol * (1 - albedo)
    abs1 = epsilon1
    abs2 = epsilon2
    Tr1 = 1.0 - abs1
    Tr2 = 1.0 - abs2
    # layer 2 budget
    # dF2/dt = abs2*Tr1*Fg + abs2*F1 - 2*F2
    # layer 1 budget
    # dF1/dt = abs1*Fg - 2*F1 + abs1*F2
    # Ground budget
    # dFg/dt = Sol - Fg + F1 + Tr1*F2
    the_array = [[abs2 * Tr1, abs2, -2.0], [abs1, -2.0, abs1], [-1.0, 1.0, Tr1]]
    the_array = np.array(the_array)
    rhs = [0, 0, -Sol]
    the_inv = linalg.inv(the_array)
    fluxes = the_inv @ rhs
    return fluxes
```

+++ {"quesnum": 3, "ctype": "answer"}

q3 answer here

```{code-cell}
---
ctype: question
papermill:
  duration: 0.006329
  end_time: '2021-06-07T20:10:58.411793'
  exception: false
  start_time: '2021-06-07T20:10:58.405464'
  status: completed
quesnum: 4
tags: []
---
def find_temps(fluxes, epsilon1=0.55, epsilon2=0.55):

    """
    Given a set of fluxes and the layer emissivities, find
    the kinetic temperature for each layer and the ground

    find_temps(fluxes,epsilon1=0.55,epsilon2=0.55)
    fluxes=(Fg,F1,F2)
    returns (Tg,T1,T2)
    """
    sigma = 5.67e-8  # W/m^2/K^4
    Tg = (fluxes[0] / sigma) ** 0.25
    T1 = (fluxes[1] / (sigma * epsilon1)) ** 0.25
    T2 = (fluxes[2] / (sigma * epsilon2)) ** 0.25
    return (Tg, T1, T2)
```

+++ {"quesnum": 4, "ctype": "answer"}

q4 answer here

+++ {"papermill": {"duration": 0.002693, "end_time": "2021-06-07T20:10:58.417152", "exception": false, "start_time": "2021-06-07T20:10:58.414459", "status": "completed"}, "tags": [], "ctype": "question", "quesnum": 5}

## compare the two functions

+++ {"quesnum": 5, "ctype": "answer"}

q5 answer here

```{code-cell}
---
ctype: question
papermill:
  duration: 0.006471
  end_time: '2021-06-07T20:10:58.426323'
  exception: false
  start_time: '2021-06-07T20:10:58.419852'
  status: completed
quesnum: 6
tags: []
---
analytic_fluxes = do_two(sol, epsilon1, albedo)
numeric_fluxes = do_two_matrix(sol, albedo, epsilon1, epsilon2)
print(f"analytic temperatures: {find_temps(analytic_fluxes)}")
print(f"numeric temperatues: {find_temps(numeric_fluxes)}")
```

+++ {"quesnum": 6, "ctype": "answer"}

q6 answer here

```{code-cell}
---
ctype: question
papermill:
  duration: 0.002918
  end_time: '2021-06-07T20:10:58.432231'
  exception: false
  start_time: '2021-06-07T20:10:58.429313'
  status: completed
quesnum: 7
tags: []
---

```

+++ {"quesnum": 7, "ctype": "answer"}

q7 answer here
