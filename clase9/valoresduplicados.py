##Eliminando valores duplicados, ejercicio 6.2.1
'''
Clase:        #9
Tema:         Listas y bucles
Ejercicio:    6.2.1. Eliminando valores duplicados
Descripción:  Dada una lista ingresada por el usuario, eliminar los elementos duplicados.

Autor:        Andrea Camila Jovel Jovel
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

lista = input("Ingresa una lista de numeros: ")

lista = list(lista.split())

lista_ordenada = []

for n in lista:
    if n not in lista_ordenada:
       lista_ordenada.append(n)
    else:
        continue


lista_ordenada = ' '.join(lista_ordenada)
print(lista_ordenada)