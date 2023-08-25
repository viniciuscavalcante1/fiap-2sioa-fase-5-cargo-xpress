import time
import random
from utils.Fila import Fila
from utils.Carga import Carga

rm = '86108'
total_mercadorias = 15
mercadorias_inseridas_na_fila = 0
fila_inicial = 3
minutos_carregar_mercadoria = (int(rm[-2:]) % 3) + 1
minutos_nova_carga_na_fila = 2
minutos_entrada_motorista = 0
tempo_espera_total = 0
ajudante = None

fila_carregar_mercadorias = Fila()
fila_total_mercadorias = Fila()


def gerar_carga(limite_carga: int) -> Fila:
    fila_total = Fila()
    for carga in range(limite_carga):
        carga = Carga()
        fila_total.enfileirar(carga)
    return fila_total


for minuto in range(100):
    print(f"######### 20h{minuto} #########")
    if minuto == 0:
        fila_total_mercadorias = gerar_carga(total_mercadorias)
        print(f"A van da empresa de logística chegou. {total_mercadorias} cargas aleatórias foram geradas...")
        time.sleep(1)
        print(f"\nVamos inserir as mercadorias na fila de carregamento. Para agilizar, vamos preparar {fila_inicial} "
              f"mercadorias de uma só vez inicialmente. A partir daí, 1 nova mercadoria será inserida a cada "
              f"dois minutos.\n")
        time.sleep(1)
        for i in range(fila_inicial):
            fila_carregar_mercadorias.enfileirar(fila_total_mercadorias.desenfileirar())
            fila_carregar_mercadorias.dados[i].set_horario_fila_de_carga(f"20h{minuto}")
            mercadorias_inseridas_na_fila += 1
            print(f"A mercadoria de ID {fila_carregar_mercadorias.dados[i]} foi adicionada à fila de carregamento às"
                  f" {fila_carregar_mercadorias.dados[i].get_horario_fila_de_carga()}."
                  f" Restam {total_mercadorias - mercadorias_inseridas_na_fila} mercadorias para serem"
                  f" adicionadas à fila."
                  f" Itens na fila até o momento: {fila_carregar_mercadorias.size()}")
            time.sleep(1)
    if ajudante is None:
        resposta_ajudante = input("\nBom, já adicionamos três mercadorias à fila! Teremos um ajudante para nos auxiliar a "
                         "carregá-las na van? Insira 'S' para SIM ou 'N' para não."
                         "\nResposta: ").upper()
        while resposta_ajudante not in ('S', 'N'):
            time.sleep(1)
            print("Por favor, insira uma resposta válida ('S' para SIM ou 'N' para não).")
            resposta_ajudante = input("Resposta: ").upper()
        if resposta_ajudante == 'S':
            ajudante = True
            time.sleep(1)
            print("Ótimo! Vai ser muito mais rápido com um ajudante. Vamos colocar mais alguns produtos "
                  "na fila, e aí, partiu carregar pra van!")
        else:
            ajudante = False
            time.sleep(1)
            print("Beleza! Vamos à guerra sem ajuda, então. Só mais uns minutos e já iniciaremos.")

    if minuto % 2 == 0 and mercadorias_inseridas_na_fila < total_mercadorias and minuto > 0:
        fila_carregar_mercadorias.enfileirar(fila_total_mercadorias.desenfileirar())
        fila_carregar_mercadorias.dados[-1].set_horario_fila_de_carga(f"20h{minuto}")
        mercadorias_inseridas_na_fila += 1
        print(f"A mercadoria de ID {fila_carregar_mercadorias.dados[-1]} foi adicionada à fila de carregamento"
              f" às {fila_carregar_mercadorias.dados[-1].get_horario_fila_de_carga()}."
              f" Restam {total_mercadorias - mercadorias_inseridas_na_fila} mercadorias para serem adicionadas à fila."
              f" Itens na fila até o momento: {fila_carregar_mercadorias.size()}")

    if minuto == 10:
        print(f"Bom, já se passaram 10 minutos! Agora são 20h{minuto} e já temos {mercadorias_inseridas_na_fila}"
              f" mercadorias na fila, uma quantidade considerável! Vamos começar a carregar!")
        time.sleep(1)
        if ajudante is True:
            print("Como temos um ajudante para nos auxiliar, podemos carregar dois produtos de uma só vez!")
            time.sleep(1)
    time.sleep(1.5)

print(gerar_carga(15))


