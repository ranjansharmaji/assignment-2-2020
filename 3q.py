import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,1,10)
y=np.zeros([len(x),2]) 

def f(y,x):
  a=y[1]
  b=x*np.exp(x)-x-y[0]+2*y[1]
  return np.array([a,b])

j=0

while j in range(9):
  h=0.1 
  k1=h*f(y[j],x[j])
  k2=h*f(y[j]+k1/2,x[j]+h/2)
  k3=h*f(y[j]+k2/2,x[j]+h/2)
  k4=h*f(y[j]+k3,x[j]+h)
  y[j+1]=y[j]+(k1+2*k2+2*k3+k4)/6
  j=j+1

plt.plot(y[:,0])

plt.xlabel('x.')
plt.ylabel('y.')
plt.legend()
plt.show()