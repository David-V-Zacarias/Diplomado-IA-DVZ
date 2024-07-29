# Solicitar confirmación para continuar
pregunta = input('Este programa calcula la categoría de impuestos de una persona basada en su salario y edad. ¿Estás seguro de continuar? (Si/No): ')

# Código
if pregunta.lower() == 'no':
    print('Programa terminado')
else:
    salario = float(input('Introduce el salario anual: '))
    edad = int(input('Introduce la edad: '))

    if salario < 20000:
        if edad < 18:
            print('Estás exento de impuestos.')
        else:
            impuesto = salario * 0.05
            print(f'Paga un 5% de impuestos: {impuesto:.2f}')
    elif 20000 <= salario <= 50000:
        impuesto = salario * 0.10
        print(f'Paga un 10% de impuestos: {impuesto:.2f}')
    else:
        impuesto = salario * 0.20
        print(f'Paga un 20% de impuestos: {impuesto:.2f}')
