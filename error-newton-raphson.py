import math


def f(x):
    return x * x - 2.0


def f1(x):
    return 2*x


def n_r(x, error, k):
    print("n       x \n")
    i = 0
    y = math.fabs(f(x))
    while i <= k and y >= error:
        print(i, k)
        x = x - (f(x) / f1(x))
        y = math.fabs(f(x))
        i = i + 1
    return x


print(n_r(2, 10 ** -5, 10))