import random

class Carga:
    def __init__(self, horario_fila_de_carga: str = None):
        self.id_carga = random.randint(0, 999)
        self.horario_fila_de_carga = horario_fila_de_carga

    def __str__(self):
        return str(self.id_carga)

    def set_horario_fila_de_carga(self, horario_fila_de_carga: str):
        self.horario_fila_de_carga = horario_fila_de_carga

    def get_horario_fila_de_carga(self):
        return self.horario_fila_de_carga
