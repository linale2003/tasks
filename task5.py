import random
from random import randint 

def matrix(o):
    k = []
    for x in range (o):
        k.append(1)
    return k

o=input('o  =')
o=int(o)
w=o
g = []
k=0

for i in range(w):
    g.append(matrix(o))
g.append([0] * (o))

for i in range(o):
    g[i-1][o-1] = g[i-1][0]
for j in range(o):
    g[w][j] = g[0][j]
    
for i in range(w):
    print(g[i])
    
for i in range(o):
    for j in range(o):
        k += g[i-1][j] * g[i+1][j]
        k += g[i-1][j] * g[i][j]
print(k)