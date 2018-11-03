def simpson(a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(0, n + 1)]
    y = [f(z) for z in x]
    sum1 = 0
    for i in range(1, n, 2):
        sum1 = sum1 + y[i]

    sum1 *= 4
    sum2 = 0
    for i in range(2, n, 2):
        sum2 = sum2 + y[i]
    sum2 *= 2
    approx = h * (y[0] + y[n - 1] + sum1 + sum2) / 3
    return approx


def f(x):
    return x ** 2


print(simpson(1, 3, 4))
