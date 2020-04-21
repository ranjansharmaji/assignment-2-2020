from scipy import integrate
import numpy as np
def f(t,y):
    dydt=np.cos(2*t)+np.sin(3*t)
    return(dydt)
sol=integrate.solve_ivp(f,[0,1],[1])
print(sol)