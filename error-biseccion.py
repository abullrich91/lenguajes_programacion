import math


def f(x):
    return x * x - 2.0


def biseccion(a, b, error, k):
    print("a m b f(a) f(m) f(b) \n")
    i = 0
    m = 0
    z = math.fabs(f(b) - f(a))
    while i <= k and z >= error:
        m = (a + b)/2
        print(a, m, b, f(a), f(m), f(b))
        if math.fabs(f(m)) < error:
            break
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
        i = i + 1
        z = math.fabs(f(b) - f(a))
    return m


print(biseccion(1, 2, 10 ** -5, 20))
