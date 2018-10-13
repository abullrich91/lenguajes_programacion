
def lagrange(xs, ys, z):
    g = ""
    s = 0
    for i in range(0, len(xs)):
        p = 1
        for k in range(0, len(xs)):
            if k != i:
                p = p * (z - xs[k]) / (xs[i] - xs[k])
                g = g + "(x - " + str(xs[k]) + ")/(" + str(xs[i]) + " - " + str(xs[k]) + ") * "
        s = s + p * ys[i]
        g = g + str(ys[i])
        if i != (len(xs)-1):
            g = g + " +"
    return s, g

from math import *
from graficador import *

def f(x):
    return exp(x)-1

X = [-2, 0, 1];
Y = [ f(X[i]) for i in range(0, len(X))];
for i in range(0, len(X)):
    #print(X[i], "\t", Y[i])
    pass

w, g = lagrange(X, Y, 1)
#print("\n", 1, "\t", w)
#print(g)
#X = 1
#print(eval(g))
print(g)

canvas = Graficador(500, 500, 30)
canvas.graficar(["exp(x)-1", g], -8, 8)

done()
