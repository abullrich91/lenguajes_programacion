from rungekutta import rungekutta


def f(x, y):
    return (x + 2) + y + 2


def g(x):
    return x + 2


def edo_rungekutta(x0, xf, y, h):
    x = x0
    ea = abs(g(x) - y)
    er = ea / g(x)
    err = er * 100
    while x < xf:
        y = rungekutta(x, y, h, f)
        x = x + h
        ea = abs(g(x) - y)
        er = ea / g(x)
        err = er * 100


edo_rungekutta(1, 10, 1, 2)
