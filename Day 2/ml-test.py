from ml import LogRegression
from math import log
import matplotlib.pyplot as plt

# ln x
x = [e * 0.5 for e in range(1, 100)]
y = [log(e) for e in x]

print(LogRegression(x, y))