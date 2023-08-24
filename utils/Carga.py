import random
class Carga:
    def __init__(self):
        self.id_carga = random.randint(0, 999)

    def __str__(self):
        return str(self.id_carga)