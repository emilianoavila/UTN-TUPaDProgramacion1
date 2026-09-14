print("Actividad 1")
print("-" * 60)

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

print(f"Precio de frutas:")
print(f"{precios_frutas}")

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(f"Precio de frutas actualizción 1:")
print(f"{precios_frutas}")

print("-" * 60)
print("Actividad 2")
print("-" * 60)

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(f"Precio de frutas actualizción 2:")
print(f"{precios_frutas}")

print("-" * 60)
print("Actividad 3")
print("-" * 60)

lista_precios_frutas = list(precios_frutas.values())

print(f"Lista solo de precio de frutas:")
print(f"{lista_precios_frutas}")

print("-" * 60)
print("Actividad 4")
print("-" * 60)

Agenda = {}

print("Agenda 5 contactos con nombre y número")

for i in range(1, 6):
    print(f"Contacto {i}:")
    Nombre = input("Ingrese el nombre: ")

    while Nombre in Agenda:
        print(f"Error, {Nombre} ya está dentro de sus contactos, elija un nombre distinto: ")
        Nombre = input("")

    numero = input("Ingrese el número de teléfono: ")

    while not numero.replace(" ", "").replace("-", "").replace("+", "").isdigit():
        print("Error, ingrese un número entero")
        numero = input("")

    Agenda[Nombre] = numero

print("Agenda actualizazada: ")
print(f"{Agenda}")

contacto = input("Escriba el nombre de un contacto para ver su número (escriba fin para terminar): ")

while not contacto.lower() == "fin":
    while not contacto in Agenda and not contacto.lower() == "fin":
        print("Error, el nombre no coincide. Escriba el nombre de un contacto para ver su número")
        contacto = input("")
        if contacto.lower() == "fin":
            break
    if contacto in Agenda:
        print(f"El número asociado a '{contacto}' es: {Agenda[contacto]}")
        break

contacto = input("Desea ver el número de otro contacto? (si/no): ")

if contacto.lower() == "si":
    contacto = input("Escriba el nombre de un contacto para ver su número: ")
    while not contacto in Agenda:
            print("Error, el nombre no coincide. Escriba el nombre de un contacto para ver su número")
            contacto = input("")
    if contacto in Agenda:
        print(f"El número asociado a '{contacto}' es: {Agenda[contacto]}")
else:
    pass

print("-" * 60)
print("Actividad 5")
print("-" * 60)

Frase = input("Ingrese una frase: ")
palabras = Frase.lower().split()
Palabras_unicas = set(palabras)

print(f"Palabras únicas encontradas: {Palabras_unicas}")

conteo_palabras = {}

for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

print(f"Recuento: {conteo_palabras}")

print("-" * 60)
print("Actividad 6")
print("-" * 60)

alumnos = {}

for i in range(1, 4):
    nombre = input(f"Ingrese el nombre del alumno {i}: ")

    print(f"Ingrese las 3 notas para {nombre}:")

    nota1 = (input("  Nota 1: "))

    while not nota1.replace(".", "").isdigit():
        print("Error, ingrese un valor numérico: ")
        nota1 = (input("  Nota 1: "))

    nota2 = (input("  Nota 2: "))

    while not nota2.replace(".", "").isdigit():
        print("Error, ingrese un valor numérico: ")
        nota2 = (input("  Nota 2: "))
    
    nota3 = (input("  Nota 3: "))

    while not nota3.replace(".", "").isdigit():
        print("Error, ingrese un valor numérico: ")
        nota3 = (input("  Nota 3: "))

    nota1 = float(nota1)
    nota2 = float(nota2)
    nota3 = float(nota3)

    alumnos[nombre] = (nota1, nota2, nota3)

print("Lista de alumnos con nota")
print(f"{alumnos}")

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    
    print(f"El promedio de {nombre} es: {promedio}")

print("-" * 60)
print("Actividad 7")
print("-" * 60)

parcial_1 = {10, 5, 7, 3, 9}
parcial_2 = {8, 4, 2, 6, 10}

print(f"Notas del primer parcial: {parcial_1}")
print(f"Notas del segundo parcial: {parcial_2}")

parcial_1.discard(5)
parcial_1.discard(3)
parcial_2.discard(2)
parcial_2.discard(4)

print(f"Notas de estudiantes que aprobaron ambos parciales: {parcial_1} {parcial_2}")

parcial_2.discard(8)
parcial_2.discard(10)

print(f"Notas de estudiantes que solo aprobaron 1 parcial: {parcial_2}")

parcial_1.add(7)
parcial_1.add(6)

print(f"Notas de estudiantes que aprobaron al menos 1 parcial: {parcial_1}")

print("-" * 60)
print("Actividad 8")
print("-" * 60)

productos_en_stock = {'Fideos': 15, 'Harina': 10, 'Jabón': 20, 'Huevos':5, 'Leche': 10}

print(f"Productos en stock: {productos_en_stock}")
stock = input("Qué desea hacer? (1-Consultar stock 2-Agregar stock 3-Agregar producto 4-Finalizar): ")

while stock != "4":
    while stock not in ["1", "2", "3", "4"]:
        print("Error, ingrese un valor que esté dentro de las opciones")
        stock = input("Qué desea hacer? (1-Consultar stock 2-Agregar stock 3-Agregar producto 4-Finalizar): ")

    if stock == "1":
        consulta = input("Escriba el nombre del producto que desea consultar el stock: ").strip().capitalize()
        while not consulta.capitalize() in productos_en_stock.keys():
            print("Error, el nombre no coincide, escriba un producto que esté en la lista")
            consulta = input("").strip().capitalize()
        print(f"El stock de {consulta} es: {productos_en_stock[consulta]}")

    if stock == "2":
        consulta = input("Escriba el nombre del producto que desea agregar el stock: ").strip().capitalize()
        while not consulta.capitalize() in productos_en_stock.keys():
            print("Error, el nombre no coincide, escriba un producto que esté en la lista")
            consulta = input("").strip().capitalize()
        stock_nuevo = input("Escriba la cantidad de stock que desea agregar: ")
        while not stock_nuevo.isdigit():
            print("Error, ingrese un valor numérico entero")
            stock_nuevo = input()
        productos_en_stock[consulta] = int(productos_en_stock[consulta]) + int(stock_nuevo)
        print(f"Lista de productos en stock actualizada {productos_en_stock}")

    if stock == "3":
        consulta = input("Escriba el nombre del producto que desea agregar: ").strip().capitalize()
        while consulta.capitalize() in productos_en_stock.keys():
            print(f"Error, {consulta} ya existe en la lista, escriba un producto que no esté en la lista")
            consulta = input("").strip().capitalize()
        nuevo_stock = input("Ingrese el stock del nuevo producto: ")
        while not nuevo_stock.isdigit():
            print("Error, ingrese un valor numérico entero")
            nuevo_stock = input("Ingrese el stock del nuevo producto: ")
        productos_en_stock[consulta] = nuevo_stock

    if stock == "4":
        break

    stock = input("Qué desea hacer? (1-Consultar stock 2-Agregar stock 3-Agregar producto 4-Finalizar): ")

print(f"Lista final: {productos_en_stock}")

print("-" * 60)
print("Actividad 9")
print("-" * 60)

Horario_UTN = {
    ("lunes", "8:00"): "Clase de Organización empresarial",
    ("lunes", "10:30"): "Clase de Matemática",
    ("martes", "8:00"): "Clase de Programación",
    ("miércoles", "8:00"): "Clase de AySO"
}

print("Horario de cursado: ")
print(Horario_UTN)

dia = input("Ingresá el día a consultar (ej: lunes): ").strip().lower()

while dia.isdigit() or dia.strip().lower() not in ["lunes", "martes", "miércoles"]:
    print("Error, ingrese un día válido")
    dia = input("")

hora = input("Ingresá la hora a consultar (ej: 10:00): ")

while not hora.replace(":", "").isdigit():
    print("Error, ingrese un horario válido")
    hora = input("")

clave_busqueda = (dia, hora)

actividad = Horario_UTN.get(clave_busqueda)

if actividad:
    print(f"El {dia} a las {hora} hay: {actividad}")
else:
    print(f"No hay ninguna actividad registrada para el {dia} a las {hora}.")

print("-" * 60)
print("Actividad 10")
print("-" * 60)

Capitales_original = {"Argentina": "Buenos Aires", "Brasil": "Brasilia", "Chile": "Santiago", "Uruguay": "Montevideo", "Perú": "Lima"}
Capitales_invertido = {capital: pais for pais, capital in Capitales_original.items()}

print("Capitales: ")
print(Capitales_original)
print("Capitales invertidas: ")
print(Capitales_invertido)