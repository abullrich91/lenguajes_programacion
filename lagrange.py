import math


def f(x):
    return math.exp(x)-1.0


def lagrange(x, y, z):
    g = ''
    s = 0
    for i in range(0, len(x)):
        p = 1
        for k in range(0, len(x)):
            if k != i:
                p = p * (z - x[k] / (x[i] - x[k]))
                g = g + " + (x - " + str(x[k]) + ") / (" + str(x[i]) + " - " + str(x[k]) + ")"
        s = s + p * f(x[i])
        g = "(" + g + ") * " + str(y[i])
    return s, g


x = [-1.0, 0.0, 2.0]
y = [f(-1), f(0), f(2)]

w, g = lagrange(x, y, 1.0)
print(g)