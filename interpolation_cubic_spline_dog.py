import math
import matplotlib.pyplot as plt
from graficador import *
import numpy as np


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
    s = [None] * (n - 1)

    for j in range(0, n):
        a[j] = (f[j])

    for i in range(0, n - 1):
        h[i] = (x[i + 1] - x[i])

    print(a[1])
    print(a[0])
    print(h[0])
    print(f1[0])

    alpha[0] = (3 * (a[1] - a[0])) / (h[0] - 3 * f1[0])
    print("alfa0", alpha[0])
    alpha[n - 1] = 3 * f1[n - 1] - (3 * (a[n - 1] - a[n - 2])) / h[n - 2]
    print("alfan", alpha[n-1])

    for i in range(1, n - 1):
        alpha[i] = ((3 / h[i]) * (a[i + 1] - a[i]) - ((3 / h[i - 1]) * (a[i] - a[i - 1])))

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

    #canvas = Graficador(500, 500, 30)
    for k in range(0, len(x) - 1):
        if k != 0:
            s="+"
        s = ""
        for j in range(0, n - 1):
            #print(a[j], "\n")
            #print(b[j], "\n")
            #print(c[j], "\n")
            #print(d[j], "\n")
            s = s + "np.add(" + str(a[j]) + ", " \
                + "np.add(np.multiply(" + str(b[j]) + ", (np.add(x, -" + str(x[j]) + "))), " \
                + "np.add(np.multiply(" + str(c[j]) + ", np.power((np.add(x, -" + str(x[j]) + ")), 2)), " \
                + "np.multiply(" + str(d[j]) + ", np.power((np.add(x, -" + str(x[j]) + ")), 3)))))"
            if j != n-2:
                s = s + "+"
            #print(s)


    #canvas.graficar(s[0:len(s)-1], 0, len(x))
    return a, b, c, d, s


x0 = [1, 2, 5, 6, 7, 8, 10, 13, 17]
x1 = [17, 20, 23, 24, 25, 27, 27.7]
x2 = [27.7, 28, 29, 30]
a0, b0, c0, d0, s0 = cubic_spline(x0, [3.0, 3.7, 3.9, 4.2, 5.7, 6.6, 7.1, 6.7, 4.5],
                              [1.0, None, None, None, None, None, None, None, -0.67])
a1, b1, c1, d1, s1 = cubic_spline(x1, [4.5, 7.0, 6.1, 5.6, 5.8, 5.2, 4.1], [3.0, None, None, None, None, None, -4.0])
a2, b2, c2, d2, s2 = cubic_spline(x2, [4.1, 4.3, 4.1, 3.0], [0.33, None, None, -1.5])

#canvas = Graficador(500, 500, 30)
#canvas.graficar(s0 + s1 + s2, 0, 31)

y0 = [s0]
y = "np.multiply(np.add(x, 1), np.add(x, 2))"
x = x0
print(s0)
plt.plot(x, eval(s0))
x = x1
plt.plot(x, eval(s1))
x = x2
plt.plot(x, eval(s2))
#use np.multiply!!!
plt.show()
