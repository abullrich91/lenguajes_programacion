from turtle import *
from math import *
import random


def graficar(f, rango):
    screensize(3000, 3000)
    c = ["red", "green", "orange", "gray", "pink", "brown"]
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

    espaciado = 10
    penup()
    goto(0, 0)
    pendown()
    puntos = 300 // espaciado
    for i in range(0, puntos + 1):
        penup()
        goto(i * espaciado, 0)
        pendown()
        dot(None, "blue")
        penup()
        goto(-i * espaciado, 0)
        pendown()
        dot(None, "blue")

    k = random.randint(0, 4)
    for j in range(len(f)):
        t = Turtle()
        t.hideturtle()
        t.color(c[k])

        x = rango[j][0];
        y0 = eval(f[j])
        t.penup()
        t.goto(x * espaciado, y0 * espaciado)
        t.pendown()
        while x <= rango[j][1]:
            y = eval(f[j]) * espaciado
            t.goto(x * espaciado, y)
            x = x + 0.1
        k = k + 1
        if k >= len(c):
            k = 0
    hideturtle()
    x = 1
    w1 = eval(f[0])
    penup()
    goto(x * espaciado, w1 * espaciado)
    pendown()
    #dot(None, "black")
    x = 1
    w2 = eval(f[1])
    penup()
    goto(x * espaciado, w2 * espaciado)
    pendown()
    #dot(None, "black")
    #write(str(w1 - w2), font=("Arial", 18, "bold"))
    done()


#graficar(["exp(x)-1", "1.486*x+0.854*x*x"], [(-2, 2), (-2, 2)])