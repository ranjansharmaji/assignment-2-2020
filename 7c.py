from scipy import integrate
def f(t,y):
    dydt=1+y/t
    return(dydt)
sol=integrate.solve_ivp(f,[1,2],[2])
print(sol)