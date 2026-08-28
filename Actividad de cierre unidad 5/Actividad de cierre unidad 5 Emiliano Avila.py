print("Actividad 1")
print("")

lista_x4 = list(range(4, 101, 4))

print ("lista de números del 1 al 100 divisibles por 4")
print(lista_x4)

print("")
print("Actividad 2")
print("")

Lista_Utiles_Escolares = ["Lapiz","Goma","Lapicera","Corrector","Regla"]

print("Lista de utiles escolares:", Lista_Utiles_Escolares)
print("Penultimo elemento de la lista:", Lista_Utiles_Escolares[-2])

print("")
print("Actividad 3")
print("")

lista_vacia = []

print("Lista vacia: ")
print("Agregue 3 elementos")

elemento1 = input("Elemento 1: ")
elemento2 = input("Elemento 2: ")
elemento3 = input("Elemento 3: ")

lista_vacia.append(elemento1)
lista_vacia.append(elemento2)
lista_vacia.append(elemento3)

print("")
print("Lista final:", lista_vacia)

print("")
print("Actividad 4")
print("")

animales = ["perro", "gato", "conejo", "pez"]

print("Lista de animales:", animales)

animales[1] = "loro"
animales[-1] = "oso"

print("Lista de animales actualizada:", animales)

print("")
print("Actividad 5")
print("")

print("Respuesta: El programa busca y elimina el número mayor de la lista, en este caso el 22, e imprime la lista sin ese número")

print("")
print("Actividad 6")
print("")

lista_x5 = list(range(10, 31, 5))

print("Lista de número entre el 10 y 30 de 5 en 5:", lista_x5)
print("Primeros 2 valores:", lista_x5[0:2])

print("")
print("Actividad 7")
print("")

autos = ["sedan", "polo", "suran", "gol"]

print("Lista de autos:", autos)

autos[1] = "casa"
autos[2] = "parque"

print("Lista de autos actualizada:", autos)

print("")
print("Actividad 8")
print("")

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print("El doble de 5, 10 y 15", dobles)

print("")
print("Actividad 9")
print("")

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

print("Lista de compras de diferentes clientes:", compras)

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print("Lista de compras actualizada:", compras)

print("")
print("Actividad 10")
print("")

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print("Lista anidada:", lista_anidada)