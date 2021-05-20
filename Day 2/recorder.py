import matplotlib.pyplot as plt
from ml import LogRegression
from time import time_ns

# operation
def add(a, b):
    return a + b

def min(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def modulo(a, b):
    return a % b

li = [1e3, 1e5, 1e9, 1e10, 1e11, 1e12, 1e13, 1e14, 1e15, 1e16]

add_record = []
min_record = []
mul_record = []
div_record = []
mod_record = []

# std of time: ns
if __name__ == '__main__':
    for a in li:
        observer = time_ns()
        add(a, a)
        add_record.append(observer%(1e6))

        observer = time_ns()
        min(a, a)
        min_record.append(observer%(1e6))

        observer = time_ns()
        mul(a, a)
        mul_record.append(observer%(1e6))

        observer = time_ns()
        div(a, a)
        div_record.append(observer%(1e6))

        observer = time_ns()
        modulo(a, a)
        mod_record.append(observer%(1e6))
    
    plt.plot(li, add_record, label="+")
    plt.plot(li, min_record, label="-")
    plt.plot(li, mul_record, label="*")
    plt.plot(li, div_record, label="/")
    plt.plot(li, mod_record, label="%")
    plt.legend()
    plt.show()

    X = [3, 5, 9, 10, 11, 12, 13, 14, 15, 16]
    print(LogRegression(X, add_record))
    print(LogRegression(X, min_record))
    print(LogRegression(X, mul_record))
    print(LogRegression(X, div_record))
    print(LogRegression(X, mod_record))
