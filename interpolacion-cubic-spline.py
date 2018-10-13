import math

f_constant = [3.0, 3.7, 3.9, 4.2, 5.7, 6.6, 7.1, 6.7, 4.5]
f1_constant = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -0.67]

def f(x):
    return f_constant[x]

def f1(x):
    return f1_constant[x]

def cubic_spline(n, x):
    alpha = [None] * n
    h = [0.0] * n
    l = [None] * n
    mu = [None] * n
    z = [None] * n
    a = [None] * n
    b = [None] * n
    c = [None] * n
    d = [None] * n

    for j in range(0, n):
        a[j] = (f(x[j]))

    for i in range(0, n-1):
        h[i] = (x[i+1] - x[i])

    alpha[0] = (3 * (a[1] - a[0])) / (h[0] - 3 * f1(x[0]))
    alpha[n-1] = 3 * f1(x[n-1]) - (3 * (a[n-1] - a[n-2])) / h[n-1]

    for i in range(1, n-1):
        alpha[i] = ((3 / h[i]) * (a[i+1] - a[i]) - ((3 / h[i-1]) * (a[i] - a[i-1])))

    l[0] = 2 * h[0]
    mu[0] = 0.5
    z[0] = alpha[0] / l[0]

    for i in range(1, n-1):
        l[i] = 2 * (x[i+1] - x[i-1]) - (h[i-1] * mu[i-1])
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - (h[i-1] * z[i-1])) / l[i]

    l[n] = h[n-1] * (2 - mu[n-1])
    z[n] = (alpha[n] - (h[n-1] * z[n-1])) / l[n]
    c[n] = z[n]

    for j in range (n-1, 0, -1):
        c[j] = z[j] - (mu[j] * c[j+1])
        b[j] = ((a[j+1] - a[j]) / h[j]) - (h[j] * (c[j+1] + 2 * c[j]) / 3)
        d[j] = (c[j+1] - c[j]) / (3 * j[j])

    for j in range(0, n-1):
        print(a[j], "\n")
        print(b[j], "\n")
        print(c[j], "\n")
        print(d[j], "\n")


cubic_spline(9, [1, 2, 5, 6, 7, 8, 10, 13, 17])