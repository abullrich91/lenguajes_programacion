el método de la secante es un algoritmo que utiliza una serie de raíces de las líneas secantes para aproximar mejor la raíz de una función f.    
    
    ''' Metodo de la Secante para encontar la raiz de una funcion
        x= lim2-f(lim2)*(lim2-lim1)/(f(lim2)-f(lim1)). Entrada de datos: lim1, lim2,
        tolerancia,numero de iteraciones maximo
    '''    
    def Secante(lim1, lim2, error, k):

    print(0,lim1,lim2)
    i=1
    while i<=k:
        x = lim2 - (lim2-lim1)*f(lim2)/(f(lim2)-f(lim1))  

        print(i, x)
        if abs(x - lim2) < error:
            return x
        i=i + 1
        lim1=lim2    # redefinir lim1
        lim2=x     #redefinir lim2

    print('El metodo fracaso despues de %d iteraciones' %k)