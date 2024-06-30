def resolver_polinomio_cuadratico(a, b, c):
    discriminante = b**2 - 4 * a * c

    if discriminante > 0:
        raiz1 = (-b + discriminante**0.5) / (2 * a)
        raiz2 = (-b - discriminante**0.5) / (2 * a)
        return raiz1, raiz2
    
    elif discriminante == 0:
        raiz = -b / (2 * a)
        return raiz, raiz
    
    else:
        parte_real = -b / (2 * a)
        parte_imaginaria = (-discriminante)**0.5 / (2 * a)
        raiz1 = complex(parte_real, parte_imaginaria)
        raiz2 = complex(parte_real, -parte_imaginaria)
        return raiz1, raiz2
    
a = 1
b = -3
c = 2

raiz1, raiz2 = resolver_polinomio_cuadratico(a, b, c)
print("Las raíces del polinomio son:", raiz1, "y", raiz2)
