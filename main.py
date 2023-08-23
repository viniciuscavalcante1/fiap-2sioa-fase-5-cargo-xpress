import time
import random
from utils.Fila import Fila
from utils.Carga import Carga

rm = '86108'
total_mercadorias = 15
ajudante = False
fila_inicial = 3
minutos_carregar_mercadoria = (int(rm[-2:]) % 3) + 1
minutos_nova_carga_na_fila = 2
minutos_entrada_motorista = 0
tempo_espera_total = 0
fila_carregar_mercadorias = Fila()

def gerar_carga(limite_carga: int) -> Fila:
    fila_total = Fila()
    for carga in range(limite_carga):
        carga = Carga()
        fila_total.enfileirar(carga)
    return fila_total


for minuto in range(100):
    print(f"20h{minuto}")
    if minuto == 0:
        fila_total_mercadorias = gerar_carga(total_mercadorias)
        print(f"A van da empresa de logística chegou. {total_mercadorias} cargas aleatórias foram geradas...")
        print(f"Vamos inserir as mercadorias na fila de carregamento. Para agilizar, vamos preparar {fila_inicial} "
              f"mercadorias de uma só vez inicialmente. A partir daí, 1 nova mercadoria será inserida a cada "
              f"dois minutos.")
        fila_carregar_mercadorias.enfileirar(fila_total_mercadorias.desenfileirar())
        print(fila_carregar_mercadorias)

    time.sleep(1.5)

print(gerar_carga(15))


