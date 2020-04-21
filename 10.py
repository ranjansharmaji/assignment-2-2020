import numpy as np
import matplotlib.pyplot as plt 

t=0
h=10
x=1
  
def f(t,x):
  return 1/(t**2+x**2)
  
j=1 
while j>=1:
  k1=h*f(t,x)
  k2=h*f(t+h/2,x+k1/2)
  k3=h*f(t+h/2,x+k2/2)
  k4=h*f(t+h,x+h)
  t=j*h
  x=x+(k1+2*k2+2*k3+k4)/6
  if t==3.5e6:
    break
  else:
    True
  j=j+1

print('x(3.5×10^6)=',x)  


   