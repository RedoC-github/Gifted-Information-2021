ans = [1849, 272400, 35]

import pandas as pd
import random as rd

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
quest2 = [e[1] for e in allavg]
quest3 = [e[2] for e in allavg]

plt.plot(range(1, n+1, 1), quest1)
plt.show()

plt.plot(range(1, n+1, 1), quest2)
plt.show()

plt.plot(range(1, n+1, 1), quest3)
plt.show()