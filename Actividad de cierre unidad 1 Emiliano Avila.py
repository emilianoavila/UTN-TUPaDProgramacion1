print("Actividad 1")
print("")

print("Hola mundo!")

print("")
print("Actividad 2")
print("")

Hola_Nombre = input("Cuál es su nombre?: ")
print(f"Hola {Hola_Nombre}!")

print("")
print("Actividad 3")
print("")

print("Introduzca su Nombre, Apeliido, Edad y Nacionalidad")
Nombre = input("Nombre: ")
Apellido = input("Apellido: ")
Edad = input("Edad: ")
Residencia = input("Pais: ")

print(f"Soy {Nombre} {Apellido}, tengo {Edad} años y vivo en {Residencia}")

print("")
print("Actividad 4")
print("")

Diametro = input("introduzca el diametro de su círculo: ")

while not Diametro.isdigit():
    print("Error, ingrese un número entero")
    Diametro = input("introduzca el diametro de su círculo: ")

Radio = int(Diametro) / 2
pi = 3.14159
Area =  int(pi * (Radio ** 2))
Perimetro = int(2 * pi * Radio)

print(f"El área del circulo es de {Area} cm y el perímetro es de {Perimetro} cm")

print("")
print("Actividad 5")
print("")

Segundos = input("introduzca una cantidad de segundos: ")

while not Segundos.isdigit():
    print("Error, ingrese un número entero")
    Segundos = input("introduzca una cantidad de segundos: ")

Horas = int(Segundos) / 60

print(f"{Segundos} segundos equivalen a {Horas} horas")

print("")
print("Actividad 6")
print("")

Multiplo = input("introduzca un número: ")

while not Multiplo.isdigit():
    print("Error, ingrese un número entero")
    Multiplo = input("introduzca un número: ")

Tabla = int(Multiplo) * 1, int(Multiplo) * 2, int(Multiplo) * 3, int(Multiplo) * 4, int(Multiplo) * 5, int(Multiplo) * 6, int(Multiplo) * 7, int(Multiplo) * 8, int(Multiplo) * 9, int(Multiplo) * 10
            
print(f"La tabla de multipliclar de {Multiplo} es {Tabla}")

print("")
print("Actividad 7")
print("")

entero1 = input("introduzca un número entero (excepto 0): ")

while not entero1.isdigit() or int(entero1) == 0:
    print("Error, debe ingresar un número entero (excepto 0)")
    entero1 = input("introduzca un número entero (excepto 0): ")

entero2 = input("introduzca otro número entero (excepto 0): ")

while not entero2.isdigit() or int(entero2) == 0:
    print("Error, debe ingresar un número entero (excepto 0)")
    entero2 = input("introduzca otro número entero (excepto 0): ")

enteros_suma = int(entero1) + int(entero2)
enteros_resta = int(entero1) - int(entero2)
enteros_division = int(entero1) / int(entero2)
enteros_multiplicacion = int(entero1) * int(entero1)

print(f"la suma de los números es {enteros_suma}")
print(f"la resta de los números es {enteros_resta}")
print(f"la multiplicación de los números es {enteros_multiplicacion}")
print(f"la división de los números es {enteros_division}")

print("")
print("Actividad 8")
print("")

Altura = input("Introduzca su altura: ")
Peso = input("Introduzca su peso: ")
Masa = int(Peso) / float(Altura) ** 2

print(f"Tu indice de masa corporal es de {Masa}")

print("")
print("Actividad 9")
print("")

Temperatura = input("Introduzca una temperatura: ")

while not Temperatura.isdigit():
    print("Error, debe ingresar un número entero")
    Temperatura = input("Introduzca una temperatura: ")

Fahrenheit = int(Temperatura) * (9 / 5) + 32

print(f"{Temperatura} grados celsius equivalen a {Fahrenheit} grados fahrenheit")

print("")
print("Actividad 10")
print("")

print("introduzca 3 números")

Primer_número = input("primer número: ")

while not Primer_número.isdigit():
    print("Error, debe ingresar un número entero")
    Primer_número = input("primer número: ")

Segundo_número = input("segundo número: ")

while not Segundo_número.isdigit():
    print("Error, debe ingresar un número entero")
    Segundo_número = input("segundo número: ")

Tercer_número = input("tercer número: ")

while not Tercer_número.isdigit():
    print("Error, debe ingresar un número entero")
    Tercer_número = input("tercer número: ")

promedio = int(Primer_número) + int(Segundo_número) + int(Tercer_número) / 3

print(f"El promedio de los números es {promedio}")