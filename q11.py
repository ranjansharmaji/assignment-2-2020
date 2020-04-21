import numpy as np
import matplotlib.pyplot as plt 

t=np.linspace(0,1,10)
h=0.1 

u=np.zeros([10,3])
u[0]=[3,-1,1]

def f(t,u):
  dw1=u[0]+2*u[1]-2*u[2]+np.exp(-t) 
  dw2=u[1]+u[2]-2*np.exp(-t)
  dw3=u[0]+2*u[1]+np.exp(-t)
  return np.array([dw1,dw2,dw3])

for j in range(9):
  k1=h*f(t[j],u[j])
  k2=h*f(t[j]+h/2,u[j]+k1/2)
  k3=h*f(t[j]+h/2,u[j]+k2/2)
  k4=h*f(t[j]+h,u[j]+k3) 
  u[j+1]=u[j]+(k1+2*k2+2*k3+k4)/6

plt.plot(t,u[:,0],label='u_1(t).')
plt.plot(t,u[:,1],label='u_2(t).')
plt.plot(t,u[:,2],label='u_3(t).')
plt.xlabel('t.')

plt.legend()
plt.show() 