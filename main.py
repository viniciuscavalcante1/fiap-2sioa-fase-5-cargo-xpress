import time
from utils.Fila import Fila
import random

def passar_10_minutos():
    ultimo_minuto = None
    for minuto in range(10):
        print(f"Tempo: 20h{minuto}")
        ultimo_minuto = minuto
    return ultimo_minuto

