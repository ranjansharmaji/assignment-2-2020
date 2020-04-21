h=0.1
y=1/3
x=0
i=1
while i in range (1,11):
    y=y+h*(-20*(y-x)*(y-x)+2*x)
    x=x+h
    i=i+1
print(y)
       