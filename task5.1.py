import random 
import numpy as np

x=int(input)
mat=np.zeros((x,x))

for i in range(x):
	for j in range(x):
		mat[i][j]=random.choice([-1,1])
print(mat)

summa=0 
for i in range(x):
	for j in range(x):
		summa+=mat[i][j]*mat[i-1][j]+mat[i][j]*mat[i][j-1]

print(summa)