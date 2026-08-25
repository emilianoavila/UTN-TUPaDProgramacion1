print("Actividad 1")
print("")

Edad = input("Introduzca su edad: ")

while not Edad.isdigit():
    print("Error, ingrese un número entero")
    Edad = input("Introduzca su edad: ")

if Edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

print("")
print("Actividad 2")
print("")

Nota = input("Introduzca su nota: ")

while not Nota.replace('.', '', 1).isdigit():
    print("Error, ingrese un valor numérico")
    Nota = input("Introduzca su nota: ")

if Nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

print("")
print("Actividad 3")
print("")

Numero_par = input("Introduzca un número par: ")

while not Numero_par.isdigit():
    print("Error, ingrese un número entero")
    Numero_par = input("Introduzca un número par: ")

while int(Numero_par) % 2 != 0:
    print("Por favor, ingrese un número par")
    Numero_par = input("Introduzca un número par: ")

if int(Numero_par) % 2 == 0:
    print("Ha ingresado un número par")

print("")
print("Actividad 4")
print("")

Edad_usuario = input("Introduzca su edad: ")

while not Edad_usuario.isdigit():
    print("Error, ingrese un número entero")
    Edad_usuario = input("Introduzca su edad: ")

if Edad_usuario < 12:
    print("Usted es un niño/a")
elif Edad_usuario >= 12 and Edad_usuario < 18:
    print("Usted es un/una adolecente")
elif Edad_usuario >= 18 and Edad_usuario < 30:
    print("Usted es un adulto/a joven")
elif Edad_usuario < 30:
    print("Usted es un adulto/a")

print("")
print("Actividad 5")
print("")

Contraseña = input("Por favor ingrese una contraseña que contenga entre 8 y 14 caracteres: ")

while len(Contraseña) < 8 or len(Contraseña) > 14:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    Contraseña = input("Contraseña: ")

if len(Contraseña) >= 8 and len(Contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")

print("")
print("Actividad 6")
print("")

from statistics import mode, median, mean

import random

numeros_aleatorios = [random.randint(1, 100) for i in range (50) ]

moda = int(mode(numeros_aleatorios))
mediana = int(median(numeros_aleatorios))
media = int(mean(numeros_aleatorios))

print(int(media))
print(int(mediana))
print(int(media))

if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
elif media == mediana and mediana == moda:
    print("No hay sesgo")
else:
    print("No hay sesgo")

print("")
print("Actividad 7")
print("")

Vocales = "aeiouAEIOU"
Palabra = input("Introduzca una palabra: ")

while any(char.isdigit() for char in Palabra):
    print("No ingrese números")
    Palabra = input("Introduzca una palabra: ")

if Palabra[-1] in Vocales:
    print(Palabra, "!")
else:
    print(Palabra)

print("")
print("Actividad 8")
print("")

Mayus = "1"
Minus = "2"
Mayus1 = "3"
Nombre = input("Introduzca su nombre con un número dependiendo de como lo desee (1 mayúsculas, 2 minúsculas, 3 primer letra en mayúscula), Ejemplo: Emiliano 1: ")

if Nombre[-1] in Mayus:
    Nombree = Nombre.replace("1", "")
    print(Nombree.upper())
elif Nombre[-1] in Minus:
    Nombree = Nombre.replace("2", "")
    print(Nombree.lower())
elif Nombre[-1] in Mayus1:
    Nombree = Nombre.replace("3", "")
    print(Nombree.title())

print("")
print("Actividad 9")
print("")

Terremoto = input("Ingrese la magnitud de un terremoto: ")

while not Terremoto.replace('.', '', 1).isdigit():
    print("Error, ingrese un valor numérico")
    Terremoto = input("Ingrese la magnitud de un terremoto: ")

if Terremoto < 3:
    print("Muy leve (imperceptible)")
elif Terremoto >= 3 and Terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif Terremoto >= 4 and Terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif Terremoto >= 5 and Terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif Terremoto >= 6 and Terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif Terremoto >= 7:
    print("Extremo  (puede causar graves daños a gran escala)")

print("")
print("Actividad 10")
print("")

Norte = "N"
Sur = "S"
Diciembre = "Diciembre"
Marzo = "Marzo"
Junio = "Junio"
Septiembre = "Septiembre"
Meses1 = "Enero", "Febrero"
Meses2 = "Abril", "Mayo"
Meses3 = "Julio", "Agosto"
Meses4 = "Octubre", "Noviembre"
Año = "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"

Hemisferio = input("Introduzca en que hemisferio se encuentra (N/S): ")

while not Hemisferio.upper() == Norte and not Hemisferio.upper() == Sur:
    print("Ingrese un hemisferio válido")
    Hemisferio = input("Introduzca en que hemisferio se encuentra (N/S): ")

Mes = input("Introduzca en que mes se encuentra, (Ej: Enero): ")

while not Mes.capitalize() in Año:
    print("Ingrese un mes válido")
    Mes = input("Introduzca en que mes se encuentra, (Ej: Enero): ")

Dia = input("Introduzca en que día se encuentra: ")

while not Dia.isdigit():
    print("Ingrese un valor numérico")
    Dia = input("Introduzca en que día se encuentra: ")

if Hemisferio in Norte and Mes in Diciembre and Dia >= 21 and Dia <= 31:
    print("Usted se encuentra en invierno")
elif Hemisferio in Norte and Mes in Meses1 and Dia >= 1 and Dia <= 31:
    print("Usted se encuentra en invierno")
elif Hemisferio in Norte and Mes in Marzo and Dia >= 1 and Dia <= 20:
    print("Usted se encuentra en invierno")
elif Hemisferio in Norte and Mes in Marzo and Dia >= 21 and Dia <= 31:
    print("Usted se encuentra en primavera")
elif Hemisferio in Norte and Mes in Meses2 and Dia >= 1 and Dia <= 31:
    print("Usted se encuentra en primavera")
elif Hemisferio in Norte and Mes in Junio and Dia >= 1 and Dia <= 20:
    print("Usted se encuentra en primavera")
elif Hemisferio in Norte and Mes in Junio and Dia >= 21 and Dia <= 31:
    print("Usted se encuentra en verano")
elif Hemisferio in Norte and Mes in Meses3 and Dia >= 1 and Dia <= 31:
    print("Usted se encuentra en verano")
elif Hemisferio in Norte and Mes in Septiembre and Dia >= 1 and Dia <= 20:
    print("Usted se encuentra en verano")
elif Hemisferio in Norte and Mes in Septiembre and Dia >= 21 and Dia <= 31:
    print("Usted se encuentra en otoño")
elif Hemisferio in Norte and Mes in Meses4 and Dia >= 1 and Dia <= 31:
    print("Usted se encuentra en otoño")
elif Hemisferio in Norte and Mes in Diciembre and Dia >= 1 and Dia <= 20:
    print("Usted se encuentra en otoño")
elif Hemisferio in Sur and Mes in Diciembre and Dia >= 21 and Dia <= 31:
    print("Usted se encuentra en verano")
elif Hemisferio in Sur and Mes in Meses1 and Dia >= 1 and Dia <= 31:
    print("Usted se encuentra en verano")
elif Hemisferio in Sur and Mes in Marzo and Dia >= 1 and Dia <= 20:
    print("Usted se encuentra en verano")
elif Hemisferio in Sur and Mes in Marzo and Dia >= 21 and Dia <= 31:
    print("Usted se encuentra en otoño")
elif Hemisferio in Sur and Mes in Meses2 and Dia >= 1 and Dia <= 31:
    print("Usted se encuentra en otoño")
elif Hemisferio in Sur and Mes in Junio and Dia >= 1 and Dia <= 20:
    print("Usted se encuentra en otoño")
elif Hemisferio in Sur and Mes in Junio and Dia >= 21 and Dia <= 31:
    print("Usted se encuentra en invierno")
elif Hemisferio in Sur and Mes in Meses3 and Dia >= 1 and Dia <= 31:
    print("Usted se encuentra en invierno")
elif Hemisferio in Sur and Mes in Septiembre and Dia >= 1 and Dia <= 20:
    print("Usted se encuentra en invierno")
elif Hemisferio in Sur and Mes in Septiembre and Dia >= 21 and Dia <= 31:
    print("Usted se encuentra en primavera")
elif Hemisferio in Sur and Mes in Meses4 and Dia >= 1 and Dia <= 31:
    print("Usted se encuentra en primavera")
elif Hemisferio in Sur and Mes in Diciembre and Dia >= 1 and Dia <= 20:
    print("Usted se encuentra en primavera")