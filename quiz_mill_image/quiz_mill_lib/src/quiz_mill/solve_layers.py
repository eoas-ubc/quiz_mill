import numpy as np
from scipy import linalg

# %%
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

# %%
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

# %%
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
