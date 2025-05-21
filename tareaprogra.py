##Ejercicios de 1.3

#Cáculo de propina

"""total_cuenta = float(input("Ingresa el total de la cuenta: $"))

porcentaje_propina = float(input("¿Cuál es el porcentaje de la propina? "))

propina = total_cuenta*(porcentaje_propina/100)
total = propina + total_cuenta

print(f"Total de la cuenta: ${total_cuenta}")
print(f"Propina: ${propina}")
print(f"Total de la cuenta con propina ({porcentaje_propina})%: ${total}")"""


#Generador de correo de Key
"""nombre = input("Ingresa tu nombre completo: ")
separar = nombre.split()

primer_name = separar[0].lower()
apellido = separar[2].lower()

print(f"El correo que se debe asignar al usuario ingresado es: \n{primer_name}.{apellido}@keyinstitute.edu.sv")"""

##Ejercicios de 2.3

#Contraseña segura

"""contraseña = input("Ingresa tu contraseña: ")

#Verificar: 8 caracteres, un numero, una mayúscula
contador_digito = 0
contador_may = 0
for i in contraseña:
    if i.isdigit():
        contador_digito += 1
    if i.isupper():
        contador_may +=1

if contador_digito > 0 and contador_may>0 and  len(contraseña )>=8:
    print("Contraseña segura")
else:
    print("Contraseña insegura")"""

#Cálculo de impuestos

unidades= int(input("Ingresa las unidades consumidas: "))

if unidades >= 0 and unidades <= 100:
    print("Impuesto aplicado: Sin impuestos")

elif unidades > 100 and unidades <= 200:
    print(f"Impuesto aplicado {unidades*0.5}")

elif unidades > 200 :
    print(f"Impuesto aplicado {unidades*0.7}")