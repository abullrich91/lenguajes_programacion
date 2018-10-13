import math
import matplotlib.pyplot as plt

def cubic_spline(n, x, f, f1):
    alpha = [None] * n
    h = [0.0] * (n-1)
    l = [None] * n
    mu = [None] * n
    z = [None] * n
    a = [None] * n
    b = [None] * n
    c = [None] * n
    d = [None] * n

    for j in range(0, n):
        a[j] = (f[j])

    for i in range(0, n-1):
        h[i] = (x[i+1] - x[i])

    alpha[0] = (3 * (a[1] - a[0])) / (h[0] - 3 * f1[0])
    alpha[n-1] = 3 * f1[n-1] - (3 * (a[n-1] - a[n-2])) / h[n-2]

    for i in range(1, n-1):
        alpha[i] = ((3 / h[i]) * (a[i+1] - a[i]) - ((3 / h[i-1]) * (a[i] - a[i-1])))

    l[0] = 2 * h[0]
    mu[0] = 0.5
    z[0] = alpha[0] / l[0]

    for i in range(1, n-1):
        l[i] = 2 * (x[i+1] - x[i-1]) - (h[i-1] * mu[i-1])
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - (h[i-1] * z[i-1])) / l[i]

    l[n-1] = h[n-2] * (2 - mu[n-2])
    z[n-1] = (alpha[n-1] - (h[n-2] * z[n-2])) / l[n-1]
    c[n-1] = z[n-1]

    for j in range(n-2, -1, -1):
        c[j] = z[j] - (mu[j] * c[j+1])
        b[j] = ((a[j+1] - a[j]) / h[j]) - (h[j] * (c[j+1] + 2 * c[j]) / 3)
        d[j] = (c[j+1] - c[j]) / (3 * h[j])

    for j in range(0, n-1):
        print(a[j], "\n")
        print(b[j], "\n")
        print(c[j], "\n")
        print(d[j], "\n")


cubic_spline(9, [1, 2, 5, 6, 7, 8, 10, 13, 17], [3.0, 3.7, 3.9, 4.2, 5.7, 6.6, 7.1, 6.7, 4.5], [1.0, None, None, None, None, None, None, None, -0.67])
cubic_spline(7, [17, 20, 23, 24, 25, 27, 27.7], [4.5, 7.0, 6.1, 5.6, 5.8, 5.2, 4.1], [3.0, None, None, None, None, None, -4.0])
cubic_spline(4, [27.7, 28, 29, 30], [4.1, 4.3, 4.1, 3.0], [0.33, None, None, -1.5])

x = [2, 4, 6]
y = [1, 3, 5]
plt.plot(x, y)
plt.show()