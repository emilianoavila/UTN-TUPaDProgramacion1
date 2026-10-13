from plato import Plato
from ingrediente import Ingrediente

def pedir_decimal(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Debe ingresar un numero valido.")

def cargar_plato():
    nombre = input("Ingrese el nombre del plato: ")
    precio = pedir_decimal("Ingrese el precio: ")
    respuesta = input("Es una bebida? (SI/NO): ")
    esBebida = respuesta.upper() == "SI"

    plato = Plato(nombre, precio, esBebida)

    if not esBebida:
        print("Carga de ingredientes (minimo 1):")
        seguir = True
        while seguir:
            nom = input("Nombre del ingrediente: ")
            cant = pedir_decimal("Cantidad: ")
            unidad = input("Unidad de medida: ")
            plato.agregar_ingrediente(Ingrediente(nom, cant, unidad))

            if len(plato.ingredientes) >= 1:
                r = input("Desea agregar otro ingrediente? (SI/NO): ")
                if r.upper() == "NO":
                    seguir = False

    return plato

def mostrar_menu(platosMenu):
    print("MENU")
    for plato in platosMenu:
        print(plato.nombreCompleto)
        print(f"Precio: ${plato.precio}")
        if not plato.esBebida:
            print("Ingredientes:")
            print("Nombre Cantidad Unidad de Medida")
            for ing in plato.ingredientes:
                print(f"{ing.nombre} {ing.cantidad} {ing.unidadMedida}")

def main():
    platosMenu = []

    seguir = True
    while seguir:
        plato = cargar_plato()
        platosMenu.append(plato)
        r = input("Desea cargar otro plato? (SI/NO): ")
        if r.upper() == "NO":
            seguir = False

    mostrar_menu(platosMenu)

if __name__ == "__main__":
    main()