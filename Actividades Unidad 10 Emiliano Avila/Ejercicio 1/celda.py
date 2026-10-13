class Celda:
    def __init__(self, fila: int, columna: int, valor: str):
        self.fila = fila
        self.columna = columna
        self.valor = valor

    def __str__(self):
        return f"Fila: {self.fila} | Columna: {self.columna} | Valor: {self.valor}"