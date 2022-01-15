import random
import numpy as np
import matplotlib.pyplot as plt
# импорт необходимых библиотек


# In[5]:


x = 6
y = [1, -1]
X_Y = range(x)
T = 0.8
m = np.zeros((x, x))
for q in range(x):
    for w in range(x):
        m[q, w] = random.choice(y)
print(m) # матрица из рандомных 1 и -1

save1 = []
save1 = m.copy()
for e in range(301):
    Summa1 = Summa2 = 0 
    for r in range(x):
        for t in range(x):
            Summa1 += m[r][t] * m[r][t-1] + m[r-1][t] * m[r][t] # сумма попарных произведений 1
    save2 = []
    save2 = m.copy()
    save2[random.choice(X_Y)][random.choice(X_Y)] *= -1
    for a in range(x):
        for b in range(x):
            Summa2 += save2[a][b] * save2[a][b-1] + save2[a-1][b] * save2[a][b] # сумма попарных произведений 2
    delE = Summa2 - Summa1   # Дельта Е
    if delE <= 0:
        m = save2.copy()
        save1 = m.copy()
    else:
        P = random.uniform(0, 1)
        W = np.exp(-delE/T)
        if P <= W:
            save1 = m.copy()
        else:
            m = save1.copy()
    print(m)
    
    plt.clf()
    plt.imshow(m)
    plt.draw()
    plt.show()
    plt.gcf().canvas.flush_events()
plt.ioff()
# вывод графически






