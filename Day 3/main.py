ans = [1849, 272400, 35]

import pandas as pd
import random as rd
from ml import LogRegression

ds = pd.read_csv('ds.csv')
data = [ds['2'].tolist(), ds['3'].tolist(), ds['4'].tolist()]

n = len(data[0])
print(data)

allavg = []

for i in range(1, n+1):
  avg = [0, 0, 0]
  for k in range(3): 
    for j in range(100):
      rd.shuffle(data[k])
      avg[k] += abs(ans[k] - (sum(data[k][:i])/i)); 
  allavg.append([e / 100 for e in avg])

print(allavg)


import matplotlib.pyplot as plt

quest1 = [e[0] for e in allavg]
mx = max(quest1)
mn = min(quest1)
quest1 = [(e-mn)/(mx-mn) for e in quest1]
quest2 = [e[1] for e in allavg]
mx = max(quest2)
mn = min(quest2)
quest2 = [(e-mn)/(mx-mn) for e in quest2]
quest3 = [e[2] for e in allavg]
mx = max(quest3)
mn = min(quest3)
quest3 = [(e-mn)/(mx-mn) for e in quest3]

plt.plot(range(1, n+1, 1), quest1)
plt.show()
LogRegression(range(1, n+1, 1), quest1)


plt.plot(range(1, n+1, 1), quest2)
plt.show()
LogRegression(range(1, n+1, 1), quest2)

plt.plot(range(1, n+1, 1), quest3)
plt.show()
LogRegression(range(1, n+1, 1), quest3)