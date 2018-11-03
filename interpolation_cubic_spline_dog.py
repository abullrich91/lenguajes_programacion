import math
import matplotlib.pyplot as plt
from graficador import *
import numpy as np
from graficador_diana import *


def cubic_spline(x, f, f1):
    n = len(x)
    alpha = [None] * n
    h = [0.0] * (n - 1)
    l = [None] * n
    mu = [None] * n
    z = [None] * n
    a = [None] * n
    b = [None] * n
    c = [None] * n
    d = [None] * n

    for j in range(0, n):
        a[j] = (f[j])

    for i in range(0, n - 1):
        h[i] = (x[i + 1] - x[i])

    alpha[0] = (3 * (a[1] - a[0])) / h[0] - 3 * f1[0]
    alpha[n - 1] = 3 * f1[n - 1] - (3 * (a[n - 1] - a[n - 2])) / h[n - 2]

    for i in range(1, n - 1):
        alpha[i] = ((3 * (a[i + 1] - a[i]) / h[i]) - (3 * (a[i] - a[i - 1])) / h[i - 1])

    l[0] = 2 * h[0]
    mu[0] = 0.5
    z[0] = alpha[0] / l[0]

    for i in range(1, n - 1):
        l[i] = 2 * (x[i + 1] - x[i - 1]) - (h[i - 1] * mu[i - 1])
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - (h[i - 1] * z[i - 1])) / l[i]

    l[n - 1] = h[n - 2] * (2 - mu[n - 2])
    z[n - 1] = (alpha[n - 1] - (h[n - 2] * z[n - 2])) / l[n - 1]
    c[n - 1] = z[n - 1]

    for j in range(n - 2, -1, -1):
        c[j] = z[j] - (mu[j] * c[j + 1])
        b[j] = ((a[j + 1] - a[j]) / h[j]) - (h[j] * (c[j + 1] + 2 * c[j]) / 3)
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    s = []
    for j in range(0, n - 1):
        #print(a[j], "\n")
        #print(b[j], "\n")
        #print(c[j], "\n")
        #print(d[j], "\n")
        s.append( str(a[j])+"+" + str(b[j])+"*(x-"+str(x[j])+")+"+\
              str(c[j])+"*(x-"+ str(x[j]) +")**2+"+str(d[j])+\
               "*(x-"+ str(x[j])+ ")**3")

    #print("s: ", s)
    return a, b, c, d, s


x0 = [1, 2, 5, 6, 7, 8, 10, 13, 17]
x1 = [17, 20, 23, 24, 25, 27, 27.7]
x2 = [27.7, 28, 29, 30]
a0, b0, c0, d0, s0 = cubic_spline(x0, [3.0, 3.7, 3.9, 4.2, 5.7, 6.6, 7.1, 6.7, 4.5],
                              [1.0, None, None, None, None, None, None, None, -0.67])
inter0 = list()
for i in range(0, len(x0) - 1):
    inter0.append((x0[i], x0[i + 1]))
a1, b1, c1, d1, s1 = cubic_spline(x1, [4.5, 7.0, 6.1, 5.6, 5.8, 5.2, 4.1], [3.0, None, None, None, None, None, -4.0])

inter1 = list()
for i in range(0, len(x1) - 1):
    inter1.append((x1[i], x1[i + 1]))
a2, b2, c2, d2, s2 = cubic_spline(x2, [4.1, 4.3, 4.1, 3.0], [0.33, None, None, -1.5])

inter2 = list()
for i in range(0, len(x2) - 1):
    inter0.append((x2[i], x2[i + 1]))

s = list()
s.extend(s0)
s.extend(s1)
s.extend(s2)
print(s)
i = list()
i.extend(inter0)
i.extend(inter1)
i.extend(inter2)
i.sort()
print(i)
graficar(s, i)
