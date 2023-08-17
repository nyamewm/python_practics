import numpy as np
import math

def f(x):
    if x[0] == 0:
        return (x[1])**2
    return (x[0]*math.log(x[0]) + x[1])**2

def dx(x):
    if x[0] == 0:
        return 0
    return 2 * (x[0]*math.log(x[0]) + x[1]) * (math.log(x[0]) + 1)

def dy(x):
    return 2 * (x[0]*math.log(x[0]) + x[1])

def grad(x):
    return np.array([dx(x), dy(x)])

x = np.array([0.1, 0.1])
result = f(x)
gamma = 1e-2

while result > 0.0001:
    x = x - grad(x) * gamma
    result = f(x)

print(x)
