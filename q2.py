h=0.1
y=1
t=1
i=1
while i in range (1,11):
    y=y+h*(y/t-y/t*y/t)
    t=t+h
    i=i+1
print(y)