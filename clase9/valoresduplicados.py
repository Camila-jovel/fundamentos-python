##Eliminando valores duplicados

lista = input("Ingresa una lista de numeros: ")

lista = list(lista.split())

lista_ordenada = []

for n in lista:
    if n not in lista_ordenada:
       lista_ordenada.append(n)
    else:
        continue
"print(lista_ordenada)"

lista_ordenada = ' '.join(lista_ordenada)
print(lista_ordenada)