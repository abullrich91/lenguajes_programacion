from trapecios import trapecios


def romberg(a, b, n):
    h = int((b - a) / 2**n)
    T = [0] * (n+1)
    for i in range(n+2):
        T[i] = trapecios(a, b, h)
        h = 2*h
    return T


print(romberg(2, 4, 4))

