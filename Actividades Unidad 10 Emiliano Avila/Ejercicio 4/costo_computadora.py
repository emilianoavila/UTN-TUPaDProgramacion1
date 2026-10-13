from computadora import Computadora
from componente_cpu import ComponenteCPU

def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un numero entero válido.")

def pedir_decimal(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Debe ingresar un numero válido.")

def cargar_computadora():
    marca = input("Ingrese la marca de la computadora: ")
    modelo = input("Ingrese el modelo: ")
    pc = Computadora(marca, modelo)

    print("Carga de componentes de CPU:")
    seguir = True
    while seguir:
        componente = input("Componente: ")
        marca_comp = input("Marca: ")
        cantidad = pedir_entero("Cantidad: ")
        precio = pedir_decimal("Precio por unidad: ")
        pc.agregar_componente(ComponenteCPU(componente, marca_comp, cantidad, precio))

        r = input("Desea agregar otro componente? (SI/NO): ")
        if r.upper() == "NO":
            seguir = False

    return pc

def mostrar_computadora(pc):
    print("Computadora")
    print(f"Marca: {pc.marca}")
    print(f"Modelo: {pc.modelo}")
    print("Componentes:")
    print("Componente Marca Cantidad Precio X Unidad SubTotal")
    for comp in pc.componenteCPU:
        print(f"{comp.componente} {comp.marca} {comp.cantidad} {comp.precio} {comp.subtotal()}")

    costo = pc.costo_total()
    sugerido = pc.precio_sugerido()
    ganancia = sugerido - costo
    print(f"Costo Total {costo}")
    print(f"El precio sugerido de venta es {costo} + {ganancia} = {sugerido}")
    print("")

def main():
    seguir = True
    while seguir:
        pc = cargar_computadora()
        mostrar_computadora(pc)

        respuesta = input("Desea cotizar una nueva computadora? (SI/NO): ")
        if respuesta.upper() == "NO":
            seguir = False
            print("Fin")

if __name__ == "__main__":
    main()
