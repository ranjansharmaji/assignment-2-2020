from scipy import integrate
import numpy as np
def f(t,y):
    dydt=t*np.e**(3*t)-2*y
    return(dydt)
y0=0
sol=integrate.solve_ivp(f,[0,1],[y0])
print(sol)