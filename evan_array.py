import numpy as np
cantidad = 10
print(f"Voy a solicitarte {cantidad} números:")
numeros =[] 
for i in range(cantidad):
    # Recuerda que range comenzará desde 0, así que imprimimos el número solicitado pero + 1
    numero = input(f"Ingresa el número {i + 1}: ")
    # Convertir a entero, pues input regresa una cadena
    numero = np.array([numero])
    # Lo agregamos al arreglo con append
    numeros.append([numero])
print("Te mostraré los números que ingresaste: ")
for numero in numeros:
    print(numero)
numeros.reverse()
print("al invertis es",numeros)
