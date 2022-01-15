from random import randint 

a=int(input())
b=int(input())

x= [[i for i in range(a)]]
for i in range (b-1):
    x+=[[i for i in range(a)]]
for j in range(b):
    for o in range(a):
        x[j-1][o-1]=randint(0,100)
        
print(x)