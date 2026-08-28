print("Actividad 1")
print("")
print("Números enteros entre 0 y 100")

x = 0

if x == 0:
    for cont in range (0,101):
        print(cont)

print("")
print("Actividad 2")
print("")

Num_en = input("Ingrese un número entero para determinar su cantidad de dígitos: ")

while not Num_en.replace('-', '', 1).isdigit():
    print ("Error, debe ingresar un valor numérico entero")
    Num_en = input("Ingrese un número entero para determinar su cantidad de dígitos: ")

print("La cantidad de dígitos que contiene su número es",len(Num_en))

print("")
print("Actividad 3")
print("")

print("Ingrese 2 números para sumar los números comprendidos entre los valores")

Valor1 = int(input("Ingrese un número entero: "))
Valor2 = int(input("Ingrese otro número entero: "))

if Valor1 > Valor2:
    Valor1, Valor2 = Valor2, Valor1

Total = 0

for numero in range(Valor1 + 1, Valor2):
    Total = Total + numero

print(f"La suma de los números entre {Valor1} y {Valor2} es: {Total}")

print("")
print("Actividad 4")
print("")

suma = 0

print("Ingrese números enteros para sumarlos en secuencia (0 para cortar): ")

while True:
    numero = input("")
    while not numero.replace('-', '', 1).isdigit():
        print("Error, debe ingresar un número entero (0 para cortar)")
        numero = input("Ingrese un número entero (0 para cortar): ")
    suma = suma + int(numero)
    if int(numero) == 0:
        break

print("El total acumulado es",(suma))

print("")
print("Actividad 5")
print("")

import random

Num_random = random.randint(0, 9)
Num_adivinado = int(input("Adivina un número entre el 0 y el 9: "))
intentos = 1

while Num_random != Num_adivinado:
    if Num_adivinado > Num_random:
        print("Intenta un número mas bajo")
        intentos = intentos + 1
        Num_adivinado = int(input("Adivina un número entre el 0 y el 9: "))
    elif Num_adivinado < Num_random:
        print("Intenta un número mas alto")
        Num_adivinado = int(input("Adivina un número entre el 0 y el 9: "))
        intentos = intentos + 1

if Num_adivinado == Num_random:
    print("Genial, has adivinado el número")
    print("En total te tomó",intentos,"intentos")

print("")
print("Actividad 6")
print("")
print("Números pares comprendidos entre 0 y 100 de forma decreciente")

y = 0

if y == 0:
    for cont_y in range (100,-2,-2):
        print(cont_y)

print("")
print("Actividad 7")
print("")
print("Escriba un número entero para sumar los números comprendidos entre 0 y su número")

Suma1 = 0
Suma2 = input("Ingrese su número: ")
Sumaa = 0

while not Suma2.isdigit():
    print("Error, debe ingresar un número entero positivo")
    Suma2 = input("Ingrese su número: ")

Suma2 = int(Suma2)

for numeroo in range(Suma1 + 1, Suma2):
    Sumaa = Sumaa + numeroo

print(f"La suma de los números entre {Suma1} y {Suma2} es: {Sumaa}")

print("")
print("Actividad 8")
print("")
print("Escribe números para determinar cuántos son pares, impares, negativos y positivos")

Num_ent = input("Ingrese números enteros: ")

while not Num_ent.replace('-', '', 1).isdigit():
    print("Error, debe ingresar solo valores numéricos enteros")
    Num_ent = input("Ingrese números enteros: ")

numeros_enteros = 0
cont_num_pos = 0
cont_num_neg = 0
cont_num_par = 0
cont_num_impar = 0

while numeros_enteros != 10: # Cambiar el valor "10" por la cantidad de números que desea ingresar, Ej: 100
    while not Num_ent.replace('-', '', 1).isdigit():
        print("Error, debe ingresar solo valores numéricos enteros")
        Num_ent = input("Ingrese números enteros: ")
    if int(Num_ent) % 2 == 0:
        cont_num_par = cont_num_par + 1
    if int(Num_ent) % 2 != 0:
        cont_num_impar = cont_num_impar + 1
    if int(Num_ent) > 0:
        cont_num_pos = cont_num_pos + 1
    if int(Num_ent) < 0:
        cont_num_neg = cont_num_neg + 1
    numeros_enteros = numeros_enteros + 1
    Num_ent = input("Ingrese números enteros: ")

print(cont_num_par,"de esos números son pares")
print(cont_num_impar,"de esos números son impares")
print(cont_num_pos,"de esos números son positivos")
print(cont_num_neg,"de esos números son negativos")

print("")
print("Actividad 9")
print("")
print("Escribe números para determinar la media de esos valores")

Num_med = input("Ingrese números enteros: ")
numeros_mediados = 0
media = int(Num_med)

while not Num_med.replace('-','',1).isdigit():
    print("Error, debe ingresar valores numéricos enteros")
    Num_med = input("Ingrese números enteros: ")

while numeros_mediados != 10: # Cambiar el valor "10" por la cantidad de números que desea ingresar, Ej: 100
    Num_med = input("Ingrese números enteros: ")
    while not Num_med.replace('-','',1).isdigit():
        print("Error, debe ingresar valores numéricos enteros")
        Num_med = input("Ingrese números enteros: ")
    numeros_mediados = numeros_mediados + 1
    media = media + int(Num_med)

media = media / numeros_mediados

print("La media de esos números es:",media)

print("")
print("Actividad 10")
print("")

Invertido = input("Escriba un número: ")

while not Invertido.replace('-', '', 1).isdigit():
    if Invertido[0] == "-":
        print("Su número invertido es:",Invertido[0] + Invertido[1:][::-1])
    else:
        print("Su número invertido es:",Invertido[::-1])