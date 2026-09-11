print("Actividad 1")
print("-" * 60)

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

print("-" * 60)
print("Actividad 2")
print("-" * 60)

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre = input("Introduzca su nombre para un saludo personalizado: ")

while nombre.isdigit():
    print("Error, por favor introduzca un nombre real")
    nombre = input("")

saludar_usuario(nombre)

print("-" * 60)
print("Actividad 3")
print("-" * 60)

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

apellido = input("Introduzca su apellido: ")

while apellido.isdigit():
    print("Error, por favor introduzca un apellido real")
    apellido = input("")
    
edad = input("Introduzca su edad: ")

while not edad.isdigit():
    print("Error, por favor introduzca una edad real")
    edad = input("")

residencia = input("Introduzca su país de residencia: ")

while residencia.isdigit():
    print("Error, por favor introduzca una residencia real")
    residencia = input("")

informacion_personal(nombre, apellido, edad, residencia)

print("-" * 60)
print("Actividad 4")
print("-" * 60)

pi = float(3.1416)

def calcular_area_circulo(radio):
    area = pi * (int(radio) * int(radio))
    print(f"El área de su círculo es de {area} cm")
    return(area)

def  calcular_perimetro_circulo(radio):
    perimetro = 2 * pi * int(radio)
    print(f"El perímetro de su círculo es de {perimetro} cm")

radio = input("Introduzca el radio de su circulo: ")

while not radio.isdigit():
    print("Error, ingrese un valor numérico entero")
    radio = input("")

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

print("-" * 60)
print("Actividad 5")
print("-" * 60)

def  segundos_a_horas(segundos):
        horas = int(segundos) / 3600
        print(f"{segundos} segundos equivalen a {horas} horas")

segundos = input("Ingrese una cantidad de segundos: ")

while not segundos.isdigit():
    print("Error, ingrese un valor numérico entero")
    segundos = input("")

segundos_a_horas(segundos)

print("-" * 60)
print("Actividad 6")
print("-" * 60)

def tabla_multiplicar(numero):
    for multiplicar in range(1,11):
        tabla = int(numero) * int(multiplicar)
        print(f"{tabla}")

numero = input("Ingrese un número: ")

while not numero.isdigit():
    print("Error, ingrese un número entero")
    numero = input("")

print(f"La tabla de multiplicar de {numero} es:")
tabla_multiplicar(numero)

print("-" * 60)
print("Actividad 7")
print("-" * 60)

def operaciones_basicas(a, b):
    a = int(a)
    b = int(b)
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

a = input("Ingrese un número entero: ")

while not a.isdigit():
    print("Error, ingrese un número entero")
    a = input("")

b = input("Ingrese otro número entero: ")

while not b.isdigit():
    print("Error, ingrese un número entero")
    b = input("")

s, r, m, d = operaciones_basicas(a, b)

print(f"Resultados de suma, resta, multiplicación y división de {a} y {b}:")
print(f"Suma: {s}")
print(f"Resta: {r}")
print(f"multiplicación: {m}")
print(f"división: {d}")

print("-" * 60)
print("Actividad 8")
print("-" * 60)

def calcular_imc(peso, altura):
    masa_corporal = float(peso) / (float(altura) * float(altura))
    print(f"El resultado de tu IMC es: {masa_corporal}")
    return masa_corporal

peso = input("Ingrese su peso: ")

while not peso.replace('.', '', 1).isdigit():
    print("Error, ingrese un valor numérico")
    peso = input("")

altura = input("Ingrese su altura: ")

while not altura.replace('.', '', 1).isdigit():
    print("Error, ingrese un valor numérico")
    altura = input("")

calcular_imc(peso, altura)

print("-" * 60)
print("Actividad 9")
print("-" * 60)

def celsius_a_fahrenheit(celsius):
    Fahrenheit = int(celsius) * (9 / 5) + 32
    print(f"{celsius} grados celsius equivalen a {Fahrenheit} grados fahrenheit")

celsius = input("Introduzca una temperatura: ")

while not celsius.isdigit():
    print("Error, debe ingresar un número entero")
    celsius = input("")

celsius_a_fahrenheit(celsius)

print("-" * 60)
print("Actividad 10")
print("-" * 60)

def calcular_promedio(a, b, c):
    promedio = int(a) + int(b) + int(c) / 3
    print(f"El promedio de los números es {promedio}")

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

calcular_promedio(Primer_número, Segundo_número, Tercer_número)