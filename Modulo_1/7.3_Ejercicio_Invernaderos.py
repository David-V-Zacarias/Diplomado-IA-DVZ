invernaderos = 1

while invernaderos <= 3:
    print(f"Invernadero {invernaderos}:")
    temperatura = float(input("Ingrese la temperatura (grados): "))
    humedad = float(input("Ingrese la humedad (%): "))
    
    if temperatura > 30 and humedad >= 30:
        print("Acción: Ventilación")
    elif temperatura > 30 and humedad < 30:
        print("Acción: Riego y ventilación")
    elif temperatura <= 30 and humedad < 30:
        print("Acción: Riego")
    elif temperatura <= 30 and humedad >= 30:
        print("No se necesitan acciones")

    invernaderos += 1
print("Análisis completo")
