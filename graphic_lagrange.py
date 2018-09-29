from turtle import *
from math import *
from lagrange import *

color("red")
# for j in range(0, len(h)):
#    f = h[j]
f = "exp(x)-1.0"
w, g = lagrange(x, y, 1.0)
h = ["exp(x)-1.0", w]
x = 0.0
yo = eval(f)


def graficar(h, desde, hasta):
    tracer(3)
    penup()
    goto(300, 0)
    right(180)
    pendown()
    forward(600)
    penup()
    goto(0, -300)
    right(90)
    pendown()
    forward(600)

    espaciado = 30
    penup()
    goto(0, 0)
    puntos = 300
    for i in range(1, puntos + 1):
        goto(i * espaciado, 0)
        pendown()
        dot(None, "blue")
        penup()

    penup()
    goto(desde * espaciado, yo * espaciado)
    pendown()
    while desde <= hasta:
        hasta = eval(f) * espaciado
        goto(desde * espaciado, hasta)
        desde = desde + 0.1
    exitonclick()


graficar(h, x, 30)
