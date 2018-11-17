
def f(x, y):
    return x + 1 + y + 2


def rungekutta(x, y, h, f):
    k1 = f(x, y)
    k2 = f(x + h / 2, y + k1 * h / 2)
    k3 = f(x + h / 2, y + k2 * h / 2)
    k4 = f(x + h, y + k3 * h)
    y = y + (k1 + 2 * k2 + 2 * k3 + k4) * h / 6
    return y


print(rungekutta(1, 2, 3, f))
