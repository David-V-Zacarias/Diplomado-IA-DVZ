num_s = 8
adivinar = False
while not adivinar:
    num_i=float(input('Inserte su intento: '))
    if num_i == num_s:
        print('Felicidades por acertar')
        break
    else:
        print('Intenta de nuevo')

