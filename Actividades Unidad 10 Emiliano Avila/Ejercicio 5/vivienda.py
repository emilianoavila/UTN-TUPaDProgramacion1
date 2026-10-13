class Vivienda:
    def __init__(self, calle: str, numero: int, manzana: str, nroCasa: int, superficieTerreno: float):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def getMetrosCuadradosCubiertos(self):
        total = 0
        for hab in self.habitaciones:
            total += hab.metrosCuadrados

        if total > self.superficieTerreno:
            raise Exception("La superficie cubierta no puede ser mayor a la superficie del terreno")

        return total