def resolver_polinomio_cuadratico():
    a = float(input("Ingrese el coeficiente a: "))
    b = float(input("Ingrese el coeficiente b: "))
    c = float(input("Ingrese el coeficiente c: "))
    
    d = b**2 - 4 * a * c
    
    if d > 0:
        r1 = (-b + d**0.5) / (2 * a)
        r2 = (-b - d**0.5) / (2 * a)
        return r1, r2
    
    elif d == 0:
        raiz = -b / (2 * a)
        return raiz, raiz
    
    else:
        parte_real = -b / (2 * a)
        parte_imaginaria = (-d)**0.5 / (2 * a)
        r1 = complex(parte_real, parte_imaginaria)
        r2 = complex(parte_real, -parte_imaginaria)
        return r1, r2

r1, r2 = resolver_polinomio_cuadratico()
print("Las raíces del polinomio son:", r1, "y", r2)

