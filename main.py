import time
import random
from typing import Dict, Any, Type

from utils.Fila import Fila
from utils.Carga import Carga
from utils.Pilha import Pilha

sleep_entre_frases = 0
sleep_entre_minutos = 0
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
pilha_mercadorias_van = Pilha()

dic_mercadorias_sendo_carregadas = {}


def gerar_carga(limite_carga: int) -> Fila:
    fila_total = Fila()
    for carga in range(limite_carga):
        carga = Carga()
        fila_total.enfileirar(carga)
    return fila_total


def set_dic_mercadorias_sendo_carregadas(item: Carga, tempo: int, dic: dict) -> dict:
    dic[item] = tempo
    return dic


def get_status_encarregamento(dic: dict, tempo: int):
    cargas_finalizadas = []
    for carga, horario_fim in dic.items():
        if horario_fim == tempo:
            cargas_finalizadas.append(carga)
    for carga in cargas_finalizadas:
        dic.pop(carga)
    return cargas_finalizadas


def carregar_mercadoria(fila_carregar_merc: Fila,
                        horario: int,
                        dic: dict,
                        pilha_merc_van: Pilha,
                        tempo_para_carregar: int,
                        ajuda: bool):
    quantidade_a_carregar = 1
    if ajuda:
        quantidade_a_carregar = 2
    for quantidade in range(quantidade_a_carregar):
        if fila_carregar_merc.size() > 0:
            mercadoria_a_carregar = fila_carregar_merc.get_inicio()
            set_dic_mercadorias_sendo_carregadas(item=mercadoria_a_carregar,
                                                 tempo=horario + tempo_para_carregar,
                                                 dic=dic)
            print(f"A mercadoria {fila_carregar_merc.get_inicio()} está saindo da fila e sendo carregada na van às"
                  f" 20h{minuto}.")
            pilha_merc_van.empilhar(fila_carregar_merc.desenfileirar())
        else:
            return


for minuto in range(100):
    print(f"######### 20h{minuto} #########")
    if minuto == 0:
        fila_total_mercadorias = gerar_carga(total_mercadorias)
        print(f"A van da empresa de logística chegou. {total_mercadorias} cargas aleatórias foram geradas...")
        time.sleep(sleep_entre_frases)
        print(f"\nVamos inserir as mercadorias na fila de carregamento. Para agilizar, vamos preparar {fila_inicial} "
              f"mercadorias de uma só vez inicialmente. A partir daí, 1 nova mercadoria será inserida a cada "
              f"dois minutos.\n")
        time.sleep(sleep_entre_frases)
        for i in range(fila_inicial):
            fila_carregar_mercadorias.enfileirar(fila_total_mercadorias.desenfileirar())
            fila_carregar_mercadorias.dados[i].set_horario_fila_de_carga(f"20h{minuto}")
            mercadorias_inseridas_na_fila += 1
            print(f"A mercadoria de ID {fila_carregar_mercadorias.dados[i]} foi adicionada à fila de carregamento às"
                  f" {fila_carregar_mercadorias.dados[i].get_horario_fila_de_carga()}."
                  f" Restam {total_mercadorias - mercadorias_inseridas_na_fila} mercadorias para serem"
                  f" adicionadas à fila."
                  f" Itens na fila até o momento: {fila_carregar_mercadorias.size()}")
            time.sleep(sleep_entre_frases)
    if ajudante is None:
        resposta_ajudante = input("\nBom, já adicionamos três mercadorias à fila! Teremos um ajudante"
                                  " para nos auxiliar a carregá-las na van?"
                                  " Insira 'S' para SIM ou 'N' para não."
                                  "\nResposta: ").upper()
        while resposta_ajudante not in ('S', 'N'):
            time.sleep(sleep_entre_frases)
            print("Por favor, insira uma resposta válida ('S' para SIM ou 'N' para não).")
            resposta_ajudante = input("Resposta: ").upper()
        if resposta_ajudante == 'S':
            ajudante = True
            time.sleep(sleep_entre_frases)
            print("Ótimo! Vai ser muito mais rápido com um ajudante. Vamos colocar mais alguns produtos "
                  "na fila, e aí, partiu carregar pra van!")
        else:
            ajudante = False
            time.sleep(sleep_entre_frases)
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
        time.sleep(sleep_entre_frases)
        if ajudante is True:
            print("Como temos um ajudante para nos auxiliar, podemos carregar dois produtos de uma só vez!")
            time.sleep(sleep_entre_frases)
        else:
            print("Não temos ajudante, então vamos carregar uma mercadoria de cada vez.")
            time.sleep(sleep_entre_frases)
        carregar_mercadoria(fila_carregar_merc=fila_carregar_mercadorias,
                            horario=minuto,
                            dic=dic_mercadorias_sendo_carregadas,
                            pilha_merc_van=pilha_mercadorias_van,
                            tempo_para_carregar=minutos_carregar_mercadoria,
                            ajuda=ajudante)
    if minuto > 10:
        mercadorias_carregadas = get_status_encarregamento(dic=dic_mercadorias_sendo_carregadas, tempo=minuto)
        if len(mercadorias_carregadas) > 0:
            for carga in mercadorias_carregadas:
                carga.set_horario_carregada(f"20h{minuto}")
                print(f"FINALIZADA: A mercadoria {carga} teve seu carregamento à van finalizado às 20h{minuto}.\n "
                      f"Esta mercadoria entrou na fila de carga às {carga.get_horario_fila_de_carga()} e"
                      f" teve seu carregamento finalizado às {carga.get_horario_carregada()}, com"
                      f" um tempo de espera total de {carga.get_tempo_de_espera()} minutos.")
        if len(dic_mercadorias_sendo_carregadas) == 0:
            if fila_carregar_mercadorias.size() == 0:
                print("FIM! CARREGAMOS TODOS OS PRODUTOS!")
                break
            else:
                carregar_mercadoria(fila_carregar_merc=fila_carregar_mercadorias,
                                    horario=minuto,
                                    dic=dic_mercadorias_sendo_carregadas,
                                    pilha_merc_van=pilha_mercadorias_van,
                                    tempo_para_carregar=minutos_carregar_mercadoria,
                                    ajuda=ajudante)
    time.sleep(sleep_entre_minutos)
