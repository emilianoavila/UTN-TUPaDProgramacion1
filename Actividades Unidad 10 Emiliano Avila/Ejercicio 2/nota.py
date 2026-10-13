class Nota:
    def __init__(self, catedra: str, notaExamen: float):
        self.catedra = catedra
        self.notaExamen = notaExamen

    def __str__(self):
        return f"Catedra: {self.catedra} - Nota: {self.notaExamen}"