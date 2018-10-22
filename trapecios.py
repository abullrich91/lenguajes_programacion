def f(x):
    return x**3


def trapecios (a, b, h):
    n = int((b - a) / h)
    x = [a + i * h for i in range(0, n+1)]
    y = [f(z) for z in x]
    t = h * (y[0] + y[n] + 2 * sum(y[1:n-1])) / 2
    return t


print(trapecios(2, 4, 0.5))
