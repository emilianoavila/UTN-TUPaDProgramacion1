# Actividad 1

archivo_productos = 'productos.txt'
linea1 = 'Lapiz,1500,10\n'
linea2 = 'Lapicera,2500,20\n'
linea3 = 'Goma,1000,15\n'

with open(archivo_productos, 'w') as archivo:
    archivo.write(linea1)
    archivo.write(linea2)
    archivo.write(linea3)

print("Actividad 2")
print("")

def imprimir_lista():
    with open(archivo_productos, 'r') as archivo:
        for linea in archivo:
            datos = linea.strip().split(',')
            if len(datos) == 3:
                nombre = datos[0]
                precio = datos[1]
                cantidad = datos[2]
                print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

imprimir_lista()

print("")
print("Actividad 3")
print("")

nuevo_producto = input("Escriba el nombre de un producto para agregarlo a la lista: ")

while nuevo_producto.isdigit():
    print("Error, ingrese un nombre válido")
    nuevo_producto = input("")

nuevo_precio = input("Escriba el precio del producto: ")

while not nuevo_precio.isdigit():
    print("Error, ingrese un valor numérico entero")
    nuevo_precio = input("")

nueva_cantidad = input("Escriba la cantidad del producto: ")

while not nueva_cantidad.isdigit():
    print("Error, ingrese un valor numérico entero")
    nueva_cantidad = input("")

with open(archivo_productos, 'a') as archivo:
    archivo.write(f"{nuevo_producto},{nuevo_precio},{nueva_cantidad}")

print("Producto guardado")

imprimir_lista()

print("")
print("Actividad 4")

productos_diccionario = []

with open(archivo_productos, 'r') as archivo:
    for linea in archivo:
        datos = linea.strip().split(',')
        if len(datos) == 3:
            diccionario_producto = {
                'nombre': datos[0],
                'precio': int(datos[1]),
                'cantidad': int(datos[2])
            }
            productos_diccionario.append(diccionario_producto)

print("\nLista de productos cargada en memoria:")
print(productos_diccionario)

print("")
print("Actividad 5")
print("")

buscado = input("Ingrese el nombre del producto a buscar: ")

encontrado = False
for prod in productos_diccionario:
    if prod['nombre'].lower() == buscado.lower():
        print(f"¡Encontrado! Producto: {prod['nombre']} | Precio: ${prod['precio']} | Cantidad: {prod['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("Error: El producto no existe en la lista.")

print("")
print("Actividad 6")
print("")

with open(archivo_productos, 'w') as archivo:
    for prod in productos_diccionario:
        linea = f"{prod['nombre']},{prod['precio']},{prod['cantidad']}"
        archivo.write(linea)

print("El archivo 'productos.txt' fue actualizado correctamente.")