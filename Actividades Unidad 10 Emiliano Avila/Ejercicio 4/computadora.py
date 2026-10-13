class Computadora:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.componenteCPU = []

    def agregar_componente(self, componente):
        self.componenteCPU.append(componente)

    def costo_total(self):
        total = 0
        for comp in self.componenteCPU:
            total += comp.subtotal()
        return total

    def precio_sugerido(self):
        costo = self.costo_total()
        if costo < 50000:
            ganancia = costo * 0.40
        else:
            ganancia = costo * 0.30
        return costo + ganancia