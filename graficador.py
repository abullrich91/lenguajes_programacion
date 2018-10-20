from turtle import *
from math import *
import __future__

class Graficador:
    def __init__(self, ancho, alto, espaciado=30):
        self.ancho = ancho
        self.alto = alto
        self.espaciado = espaciado
        self.colores = ["red", "blue", "green"]

    def graficar(self, h, desde, hasta):
        clearscreen()
        tracer(3)
        penup()
        goto(self.ancho/2, 0)
        right(180)
        pendown()
        forward(self.ancho)
        penup()
        goto(0, -self.alto/2)
        right(90)
        pendown()
        forward(self.alto)
        penup()
        goto(0, 0)
        puntos = floor((self.ancho/2) // self.espaciado)
        for i in range(-puntos, puntos + 1):
            goto(i * self.espaciado, 0)
            pendown()
            tam = 8 if (i % 5 == 0) else 4
            dot(tam, "black")
            penup()
            pass
        puntos = floor((self.alto/2) // self.espaciado)
        for i in range(-puntos, puntos + 1):
            goto(0, i * self.espaciado)
            pendown()
            tam = 8 if (i % 5 == 0) else 4
            dot(tam, "black")
            penup()
            pass
        for k in range(0, len(h)):
            x = desde
            ht()
            y0 = eval(h[k])
            penup()
            goto(x * self.espaciado, y0 * self.espaciado)
            pendown()
            color(self.colores[k % len(self.colores)])
            while x <= hasta:
                y = eval(h[k])
                goto(x * self.espaciado, y * self.espaciado)
                x = x + 0.1
            pass
