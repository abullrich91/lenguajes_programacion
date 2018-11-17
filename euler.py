def f(x, y):
    return x + 1 + y + 2


def euler(f, xa, xb, ya, n):
    h = (xb - xa) / float(n)
    x = xa
    y = ya
    for i in range(n):
        y = y + h * f(x, y)
        x = x + h
    return y


print(euler(f, 1, 5, 3, 100))
