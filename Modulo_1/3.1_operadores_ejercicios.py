"""
Escribir un programa que solicite dos números y luego imprima:
    1. La suma de dos números
    2. La reta del primer número menos el segundo
    3. El producto de los dos números 
    4. El cubo de la suma de los dos números
    5. El cociente de la división del primer número por el segundo. 
"""
num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))

print(f'Suma:', num1+num2)
print(f'Resta:', num1-num2)
print(f'Producto:', num1*num2)
print(f'Cubo de la suma:',(num1+num2)**3)
print(f'División:', (num1/num2))