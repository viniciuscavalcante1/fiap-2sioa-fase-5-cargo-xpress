import random

class Carga:
    def __init__(self, horario_fila_de_carga: str = None, horario_carregada: str = None):
        self.id_carga = random.randint(0, 999)
        self.horario_fila_de_carga = horario_fila_de_carga
        self.horario_carregada = horario_carregada

    def __str__(self):
        return str(self.id_carga)

    def set_horario_fila_de_carga(self, horario_fila_de_carga: str):
        self.horario_fila_de_carga = horario_fila_de_carga

    def set_horario_carregada(self, horario_carregada: str):
        self.horario_carregada = horario_carregada

    def get_horario_fila_de_carga(self):
        return self.horario_fila_de_carga

    def get_horario_carregada(self):
        return self.horario_carregada

    def get_tempo_de_espera(self):
        return (int(self.get_horario_carregada().replace("20h", ""))
                - int(self.get_horario_fila_de_carga().replace("20h", "")))
