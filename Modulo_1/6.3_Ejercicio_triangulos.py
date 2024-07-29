# Solicitar confirmación para continuar
pregunta = input('Este programa determina el tipo de triángulo basado en las longitudes de sus lados. ¿Estás seguro de continuar? (Si/No): ')

# Código
if pregunta.lower() == 'no':
    print('Programa terminado')
else:
    lado1 = float(input('Introduce la longitud del primer lado: '))
    lado2 = float(input('Introduce la longitud del segundo lado: '))
    lado3 = float(input('Introduce la longitud del tercer lado: '))

    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        if lado1 == lado2 == lado3:
            print('El triángulo es equilátero.')
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print('El triángulo es isósceles.')
        else:
            print('El triángulo es escaleno.')
    else:
        print('Las longitudes introducidas no forman un triángulo válido.')
