import math


def c(t):
    return 80 * math.exp(-2*t) + 20 * math.exp(-0.5*t)


def c1(t):
    return 80 * (-2) * math.exp(-2*t)


def n_r_bacterias(x, error, k, limit):
    print("n       x \n")
    hours = 0
    i = 0
    y = c(hours)
    while i <= k and y >= error and x >= limit:
        print(i, k)
        x = x - math.fabs(c(hours) / c1(hours))
        y = math.fabs(c(hours))
        i = i + 1
        hours = hours + 0.5
    return hours


print(n_r_bacterias(10000, 10 ** -5, 50, 7))
