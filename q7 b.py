from scipy import integrate
def f(t,y):
    dydt=1-(t-y)*(t-y)
    return(dydt)
sol=integrate.solve_ivp(f,[2,3],[1])
print(sol)