'''
Clase:        #5
Tema:         Bucles
Ejercicio:    5.4.1. Sumador de valores posicionales
Descripción: Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito. Ejemplo:
Si el usuario ingresa 9875, entonces: 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2.

Autor:        Andrea Camila Jovel Jovel
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''



numero = int(input("Ingresa un numero: "))
print(f"\nProceso de reducción para {numero}:")


while numero > 9: # los numero mayores a 9 tienen 2 digitos por lo que entran al for
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    
    print(f"{numero} = {suma}")
    numero = suma

print(f"\nResultado final: {numero}")

    
