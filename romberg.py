from trapecios import trapecios


def romberg(a, b, N):
    h = b - a
    i = 0
    t = []
    while i <= N:
        t.append(trapecios(a, b, h))
        i = i + 1
        h = h / 2
    print("P0: ", t)
    t = t[::-1]
    j = 1
    c = 4
    while j <= N:
        i = 0
        while i <= N - j:
            print("t[i]: ", t[i], "t[i+1]: ", t[i + 1])
            t[i] = (c * t[i] - t[i + 1]) / (c - 1)
            i = i + 1
        print("P" + str(j) + ": ", t)
        j = j + 1
        c = c * 4

    return t[0]


print(romberg(2.0, 4.0, 4))

