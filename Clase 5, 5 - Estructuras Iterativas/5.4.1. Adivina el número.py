'''
Clase:        #5
Tema:         Bucles
Ejercicio:    5.4.1. ¡Adivina el número!
Descripción: Genera un número aleatorio entre 1 y 100 y pide al usuario que lo adivine.
El programa debe seguir pidiendo números hasta que acierte.

Autor:        Andrea Camila Jovel Jovel
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''

import random 

num_aleatorio = numero_aleatorio = random.randint(1, 100)


while True:

    intento = int(input("Ingresa un numero entre 1 y 100: "))

    if intento == num_aleatorio:
        print(f"¡Felicidades! Has adivinado el numero secreto: {numero_aleatorio}")
        print("Fin del juego")
        break 
    if num_aleatorio>intento:
        print("El número secreto es mayor")
    else:
        print("El numero secreto es menor")
    
    
    


