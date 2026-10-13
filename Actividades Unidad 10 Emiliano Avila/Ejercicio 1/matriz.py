from celda import Celda

class Matriz:
    def __init__(self):
        self.celdasMatriz = []

    def existe_celda(self, fila, columna):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return True
        return False

    def agregar_celda(self, celda):
        if self.existe_celda(celda.fila, celda.columna):
            return False
        self.celdasMatriz.append(celda)
        return True

    def mostrar_celdas(self):
        if len(self.celdasMatriz) == 0:
            print("No se cargaron celdas.")
        for celda in self.celdasMatriz:
            print(celda)

    def obtener_valor(self, fila, columna):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor
        return "La fila y columna indicada no ha sido asignada en ninguna celda"
