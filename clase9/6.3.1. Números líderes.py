'''
Clase:        #6
Tema:         Listas y bucles
Ejercicio:    6.3.1 Números líderes
Descripción: Un número en una lista es "líder" si es
estrictamente mayor que todos los
elementos a su derecha. Dada una lista de
números ingresada por el usuario, imprime
todos los números líderes.

Autor:       Andrea Camila Jovel Jovel
Fecha:        2025-06-02
Estado:       [ Terminado ]
'''
numero = input("Entrada:\n")

numeros_lista = list(map(int, numero.split()))
lista = []

for i in range(len(numeros_lista)-1):
    es_lider = True
    for j in range(i + 1, len(numeros_lista)):
        if numeros_lista[i] <= numeros_lista[j]:
            es_lider = False
            break
    if es_lider:
        lista.append(numeros_lista[i])
        
print("Salida:")
print(" ".join(map(str, lista)))

        

    


