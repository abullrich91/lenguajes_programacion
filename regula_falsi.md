=====Regula Falsi=====

Este método consiste en encontrar la raíz de una función, teniendo en cuenta los intervalos de la función, y que el error debe ser menor al 1%.

El método combina el método de bisección y el método de la secante.

Como en el método de bisección, se parte de un intervalo inicial [a0,b0] con f(a0) y f(b0) de signos opuestos, lo que garantiza que en su interior hay al menos una raíz (véase Teorema de Bolzano). El algoritmo va obteniendo sucesivamente en cada paso un intervalo más pequeño [ak, bk] que sigue incluyendo una raíz de la función f.

la función de regula-falsi es: 
    
    r = a * f(b) - b * f(a)
        -------------------- 
            f(b) - f(a)
            
Esta función nos brinda un punto interior del intervalo [ak, bk]. Dicho punto es la intersección de la recta que pasa por (a,f(ak)) y (b,f(bk)) con el eje de abscisas (igual a como se hace en el método de la secante).
            
Un ejemplo de código de esta función sería:

    def regula_falsi(lim1, lim2, error):
    # Verifico que el intervalo inicial cumpla la condición de ser de signo opuesto
    if func(lim1) * func(lim2) < 0:
        i=0
        # Verifico que el error relativo sea mayor al error permitido
        while abs((lim2 - lim1) / lim2) > error and i <= 100:
            root = (lim1 * func(lim2) - lim2 * func(lim1)) / (func(lim2) - func(lim1))
            if func(lim1) * func(root) < 0:
                lim2 = root
            else:
                lim1 = root
            i=i+1
            print(i," ",root)
        return root
    else:
        return 'En ningún momento para por el eje X!'