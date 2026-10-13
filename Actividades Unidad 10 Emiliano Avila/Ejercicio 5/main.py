from barrio import Barrio
from vivienda import Vivienda
from habitacion import Habitacion

def main():
    barrio = Barrio("Las Lomas", "Constructora Mendoza SA")

    v1 = Vivienda("San Martin", 100, "A", 1, 300.0)
    v1.agregar_habitacion(Habitacion("Cocina", 20.0))
    v1.agregar_habitacion(Habitacion("Dormitorio", 25.0))
    v1.agregar_habitacion(Habitacion("Living", 30.0))
    barrio.agregar_vivienda(v1)

    v2 = Vivienda("San Martin", 102, "A", 2, 250.0)
    v2.agregar_habitacion(Habitacion("Cocina", 18.0))
    v2.agregar_habitacion(Habitacion("Dormitorio", 22.0))
    barrio.agregar_vivienda(v2)

    v3 = Vivienda("Belgrano", 50, "B", 1, 400.0)
    v3.agregar_habitacion(Habitacion("Cocina", 25.0))
    v3.agregar_habitacion(Habitacion("Dormitorio 1", 20.0))
    v3.agregar_habitacion(Habitacion("Dormitorio 2", 20.0))
    v3.agregar_habitacion(Habitacion("Living Comedor", 40.0))
    barrio.agregar_vivienda(v3)

    print(f"Barrio: {barrio.nombre} (Constructora: {barrio.empresaConstructora})")
    print()

    print(f"a) Superficie total de terreno del barrio: {barrio.getSuperficieTotalTerreno()} m2")

    print(f"b) Superficie total de terreno de la manzana A: {barrio.getSuperficieTotalTerrenoXManzana('A')} m2")

    print("c) Metros cuadrados cubiertos por vivienda:")
    for vivienda in barrio.viviendas:
        try:
            cubiertos = vivienda.getMetrosCuadradosCubiertos()
            print(f"   {vivienda.calle} {vivienda.numero} (Mz {vivienda.manzana}): {cubiertos} m2")
        except Exception as e:
            print(f"   Error en {vivienda.calle} {vivienda.numero}: {e}")

    print(f"d) Superficie total cubierta del barrio: {barrio.getSuperficieTotalCubierta()} m2")

if __name__ == "__main__":
    main()
