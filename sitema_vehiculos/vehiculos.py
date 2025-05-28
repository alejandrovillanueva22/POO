import datetime


class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca= marca
        self.modelo= modelo
        self.anio= anio
    def mostrar_info(self):
        print(f"Este auto es un {self.marca}, {self.modelo}, {self.anio}")
    def cumplir_anio(self):
        from datetime import datetime
        anio_actual= datetime.now().year
        antiguedad = anio_actual - self.anio
        print(f"Este modelo de lanzo hace {antiguedad} anios")
    