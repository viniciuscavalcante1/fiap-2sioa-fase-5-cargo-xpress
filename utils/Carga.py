import random
class Carga:
    def __init__(self):
        self.id_carga = int((random.random()) * 1000)

    def __str__(self):
        return str(self.id_carga)