from graficador import Graficador
import matplotlib.pyplot as plt
import numpy as np


def spline (x,a,n,FPO,FPN):
    m = n+1
    alfa = [0]*m
    l = [0]*m
    u = [0]*m
    z = [0]*m
    h = [x[i+1] - x[i] for i in range(0,n)]
    alfa[0] = 3*(a[1]-a[0])/h[0] - 3*FPO
    print("alfao",alfa[0])
    alfa[n] = 3*FPN - 3*(a[n]-a[n-1])/h[n-1]
    print("alfan", alfa[n])
    for  i in range(1,n):
        alfa[i] =  3*(a[i+1]-a[i])/h[i] - 3*(a[i]-a[i-1])/h[i-1]
    l[0] = 2*h[0]
    u[0] = 0.5
    z[0] = alfa[0]/l[0]
    for i in range(1,n):
        l[i] = 2*(x[i+1] - x[i-1])- h[i-1]*u[i-1]
        u[i] = h[i] /l[i]
        z[i] = (alfa[i] - h[i-1]*z[i-1])/l[i]
    l[n] = h[n-1] *(2-u[n-1])
    z[n] = (alfa[n]-h[n-1]*z[n-1])/l[n]
    c = [0]*m
    b = [0]*m
    d = [0]*m
    c[n] = z[n]
    for j in range(n-1,-1,-1):
        c[j] = z[j] - u[j]*c[j+1]
        b[j] = (a[j+1]-a[j])/h[j] - h[j] *(c[j+1]+2*c[j])/3
        d[j] = (c[j+1]-c[j])/(3*h[j])
    #print(a)
    #print(b[0:n])
    #print(c[0:n])
    #print(d[0:n])
    s = list()
    for i in range(0,n):
        s.append( str(a[i])+"+" + str(b[i])+"*(x-"+str(x[i])+")+"+\
                 str(c[i])+"*(x-"+ str(x[i]) +")**2+"+str(d[i])+\
                  "*(x-"+ str(x[i])+ ")**3")
        # s.append(str(a[i]) \
        #          + " + np.multiply(" + str(b[i]) + ", np.add(x, -" + str(x[i]) + "))"
        #          + " + np.multiply(" + str(c[i]) + ", np.power(np.add(x, -" + str(x[i]) + "), 2))" \
        #          + " + np.multiply(" + str(d[i]) + ", np.power(np.add(x, -" + str(x[i]) + "), 3))")
        #print(s[i])
        #plt.plot(x, eval(s[i]))
    inter = list()
    for i in range(0,len(x)-1):
        inter.append((x[i],x[i+1]))
    #plt.plot(s,inter)
    #print("a: ", a)
    #print("b: ", b)
    #print("c: ", c)
    #print("d: ", d)
    print("s: ", s)
    return a, b, c, d, s

canvas = Graficador(3000, 3000, 30)
a0, b0, c0, d0, s0 = spline([1,2,5,6,7,8,10,13,17] ,[3.0,3.7,3.9,4.2,5.7,6.6,7.1,6.7,4.5],8,1.0,-0.67)
a1, b1, c1, d1, s1 = spline([17,20,23,24,25,27,27.7],[4.5,7.0,6.1,5.6,5.8,5.2,4.1],6,3.0,-4.0)
a2, b2, c2, d2, s2 = spline([27.7,28,29,30],[4.1,4.3,4.1,3.0],3,0.33,-1.5)

s = s0 + s1 + s2
canvas.graficar(s, 0, 31)

plt.show()