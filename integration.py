import numpy as np


def myfunc(x):
    y = -(x - 2)**2 + 4
    return y


def mytrapz(x,y):
    h = x[1] - x[0]
    result = 0.5*h*(y[0] + y[-1] + 2*np.sum(y[1:-1]))
    return result


# Choose integration limits (a,b) and number of points N
a = 0
b = 4
N = 100

# Integrate myfunc using mytrapz
x = np.linspace(a, b, N)
integral = mytrapz(x, myfunc(x))
print(integral)



