# Solicitar edad
pregunta = input('Este programa solo acepta edades en formato de número entero, ¿estás seguro de continuar? (Si/No): ')

# Código
if pregunta == 'No':
    print('Programa terminado')
else:
    edad = int(input('Introduce la edad: '))
    if edad < 13:
        print('Niño')
    elif edad < 18:
        print('Adolescente')
    elif edad < 65:
        print('Adulto')
    else:
        print('Adulto mayor')
