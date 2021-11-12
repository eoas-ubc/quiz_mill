---
jupytext:
  cell_metadata_filter: all
  formats: ipynb,md:myst
  notebook_metadata_filter: all,-language_info,-toc,-latex_envs
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
orig_nbformat: 4
---

Name (Last, First):
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Student Number:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Signature:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**This is exam packet (A)**

**Verify that (A) in the ``Test Form'' column of your bubble sheet has been marked**

**Instructions:** You may detach the Bubble sheet (first page) and the
Equation Sheet (last page) from this exam package. No notes, books,
cellphones or aids are allowed. Calculators are okay.
Only answers indicated on the provided Bubble sheet will be marked.
You must submit both this ``question book'' as well as the Bubble sheet
before leaving the room.  For numerical questions, choose the closest answer.

+++

1\.   Of the following options, which BEST describes what greenhouse gases  
    do?  
 
   **A) Absorb and emit longwave radiation**  
   B) Reflect and emit longwave radiation  
   C) Absorb and reflect longwave radiation  
   D) Reflect and transmit longwave radiation  
   E) Absorb shortwave and emit longwave radiation

+++ {"ctype": "answer", "quesnum": 5}

q1 answer  
 
A) Absorb and emit radiation

+++ {"ctype": "question", "quesnum": 6}

 
2\.  The two walls above are in thermal equilibrium. Approximately how    much flux is absorbed by the left wall given its emissivity is  
   0.7? (wall transmissivities=0)  
 
   A) 100 $W m^{-2}$  
   B) 150 $W\,m^{-2}$  
   C) 200 $W\,m^{-2}$  
   **D) 250 $W\,m^{-2}$**  
   Ε) 300 $W\,m^{-2}$
   
<img src=figures/two_walls.png width=40%>


   
Answer D)  It is emitting 250 W/m2 (see below) The wall can't change its temperature because of the 2nd law, so it has
to absorb as much as it emits

```{code-cell} ipython3
:ctype: answer
:quesnum: 6
:trusted: true

# q2  answer 
  
# D) 250 $W\,m^{-2}$  
  
sigma = 5.67e-8
T_wall = 280  
abs = 0.7*sigma*T_wall**4.  
print(f"Q2: absorbed flux is {abs:5.1f} W/m^2 or about 250 W/m^2")  
```

+++ {"ctype": "question", "quesnum": 7}

3\.  We direct a visible beam of light at a semi-transparent sheet of glass with longwave emissivity $\epsilon_{lw}$=0.6 and shortwave reflectivity of $\alpha_{sw}$=0.2. We observe a shortwave flux $I = 100\ W/m^{2}$ on the other side of the glass. What is the value of the incident visible radiation $I_{0}$?  
 
<img src=figures/transmission.png width=45%>


   A) $40\ W/m^{2}$  
   **B) $125\ W/m^{2}$**  
   C) $155\ W/m^{2}$  
   D) $200\ W/m^{2}$  
   E) None of the above

+++

Answer B  -- By definition  Z$I_1 = \epsilon I_0$  (where we are using Kirchoff's law to write the
absorptivity as the emissivity.

```{code-cell} ipython3
:ctype: answer
:quesnum: 7
:trusted: true

# q3 answer here  
# B) 125 W/m^2  
  
100/0.8  
```

+++ {"ctype": "question", "quesnum": 9}

4\.   The following figure shows an atmosphere that is **black** in the  
    long wave, **transparent** in the visible, over a surface that  
    appears black at all wavelengths. If the ground is at $290$ K and  
    the system is in equilibrium, approximately what is the temperature of the  
    atmosphere?  
 
<img src=figures/black_atm.png width=45%>
 
   A) 245 K  
   B) 270 K  
   C) 290 K  
   D) 305 K  
   E) 320 K

+++

A) about 245 K -- We know that the system is in equilibrium, so fluxes must be in balance at
both the top and bottom levels.  that means that $I_a$ = - $I_{in}$ at the top, and $I_g$ = -2 $I_{in}$ at
at the bottom.  We know $I_g$ since we are given $T_g$.

```{code-cell} ipython3
:ctype: answer
:quesnum: 9
:trusted: true

# q4 answer here  
  
# A) 242 K  
  
T_g=290  
I_a = sigma*(T_g**4)/2.  
T_a = (I_a/sigma)**0.25  
print(f"Q4: Atmospheric flux is {I_a:5.1f} W/m^2, atmospheric temperature is {T_a:5.1f} K")  
```

+++ {"ctype": "question", "quesnum": 10}

5\.  This graph shows the flows of carbon into and out of the atmosphere since 1900. Using the information on the graph, identify all **CORRECT** statements from the list below.  

<img src=figures/stock_flow.png width=45%>
 
   i. The stock of C in the atmosphere has increased continually since 1900.  
   ii. The stock of C in the atmosphere is currently higher than it has  
       been at any time since 1900.  
   iii. From 1900 to about 1950, the stock of C in the atmosphere remained  
        constant.  
   iv. The rate at which C has been accumulating has remained approximately  
       constant since 1900.  
   v. Around 1970s, there was an abrupt drop in the stock of C.  
 
   **A) i, ii**  
   B) i, ii, v  
   C) i, ii, iv  
   D) ii, iii, iv  
   E) iii, iv, v

+++ {"ctype": "answer", "quesnum": 10}

q5 answer    **A) i, ii**  inflow is always larger than outflow, so stock has been increasing since 1800.

+++

6\. A star with a radius of 500 million m ($5 \times 10^8$ meters) has a surface temperature of 7000 K.  What is the total flux, in $W\,m^{-2}$ reaching a planet
    orbiting at a distance of 200 million km ($2 \times 10^{11}$ meters) from the star?
    
 A) 150 $W/m^2$   
 B) 450 $W/m^2$   
 C) 850 $W/m^2$   
 D) 1250 $W/m^2$   
 E) 1500 $W/m^2$

+++

Answer B -- 850 W/m^2. First find the flux using Stefan Boltzman, then find the power going through  the star's
surface (in Watts).  Then since power is conserved heading out to the planent, find the flux at the planet by spreading that power on to the sphere area at the planet's
orbit.

```{code-cell} ipython3
:trusted: true

# temp=5778.
temp=7000
flux=sigma*temp**4.
# star_rad=7.e8
star_rad = 5.e8
# distance=150.e9
distance=2.e11
power = flux*4*3.14*star_rad**2.
area = 4*3.14*distance**2.
power/area
```

7\.  Consider this figure, with two black (in the longwave, but transparent in the shortwave) layers with temperatures $T_2=250$ K and $T_1$=280 K and a surface temperature $T_G$=310 K

<img src=figures/two_black_layers.png width=45%>

What is the greenhouse effect of this atmosphere, in $W/m^2$? 

 A) 60 $W/m^2$  
 B) 100 $W/m^2$    
 C) 160 $W/m^2$  
 D) 210 $W/m^2$  
 E) 300 $W/m^2$

+++

Answer E) -- about 300 W/m^2.  -- remember it's top - bottom, subtract A2 - G:

```{code-cell} ipython3
:trusted: true

T1=280
T2=250
Tg=310
greenhouse = -sigma*T2**4. - (-sigma*Tg**4.)
print(f"{greenhouse=:5.1f} W/m^2")
```

8\. For the same setup as the previous question, what is the heating rate of layer 2?

 A) -150 $W/m^2$   
 B) -100 $W/m^2$    
 C) 0 $W/m^2$  
 D) +100 $W/m^2$    
 E) +150 $W/m^2$

+++

Subtract the bottom from the top, accounting for signs and rearrange.
Note that the answer agrees with intuition -- it's losing energy out the top and the bottom
(first term) and gaining energy by absorbing the flux from layer 1 (second term).

```{code-cell} ipython3
:trusted: true

heating_rate = -2.*sigma*T2**4.  - (-sigma*T1**4.)
print(f"{heating_rate=:5.1f} W/m^2")
```

9\. A planet that rotates like the Earth receives $S_0$ = 1500 $W/m^2$ from its sun, but reflects 50% of the incoming shortwave radiation.  What is its equilibrium surface temperature, assuming no greenhouse effect from
its atmosphere?

 A) 240 K  
 B) 280 K  
 C) 300 K  
 D) 320 K  
 E) 340 K

+++

Answer A) -- spread S0 over both hemispheres, after removing 50% due to reflection

```{code-cell} ipython3
:trusted: true

flux = 1500*0.5/4.
temp = (flux/sigma)**0.25
print(f"{temp=:5.1f} K")
```

+++ {"ctype": "equation_sheet"}

# Equation Sheet  
 
Layer energy equation:  $\frac{d E}{d t}=I_{\downarrow}+I_{\uparrow}$  
 
Solar constant  $S=\frac{S_{0}}{4}(1-\alpha)$  
 
Total grey-body flux:  $I=\varepsilon \sigma T^{4}$  
 
*where*  $\sigma=5.67 \times 10^{-8} \mathrm{Wm}^{-2} \mathrm{K}^{-4}$  
 
Transmissivity tr: $I_{\text {transmitted }}=\mathrm{tr}I_{0}$  
 
Reflectivity α:  $I_{\text {reflected }}=\alpha I_{0}$  
 
Absorptivity abs:  $I_{\text{absorbed }} = \text{abs} I_{0}$  
 
Conservation of energy:  $\alpha \mathrm{I}_{0}+ \text{abs} \mathrm{I}_{0}+\mathrm{trI}_{0}=\mathrm{I}_{0}$  
 
Kirchoff's law: $\epsilon=\text{abs}$  

$CO_2$ forcing: $$\Delta F=\left(3.8 \mathrm{W} \mathrm{m}^{-2}\right) \frac{\ln (\text { newp } \mathrm{CO} 2 / \text { origp } \mathrm{CO} 2)}{\ln (2)}$$
 
**$CO_{2}$ constants**:  
 
12 g C = 44 g $CO_{2}$  
 
7.6 gigatonnes $CO_{2}$ = 1 ppm atmospheric $CO_{2}$ concentration

```{code-cell} ipython3

```
