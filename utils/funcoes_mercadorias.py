from utils.Fila import Fila
from utils.Carga import Carga
from utils.Pilha import Pilha
import time


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
            print_letra_por_letra(
                f"\n[20h{horario} - MERCADORIA SAINDO DA FILA DE CARREGAMENTO E SENDO CARREGADA PARA A VAN: "
                f"{fila_carregar_merc.get_inicio()}]\n"
                f"\tItens na fila no momento: {fila_carregar_merc.size()}\n")
            pilha_merc_van.empilhar(fila_carregar_merc.desenfileirar())
        else:
            return


def print_letra_por_letra(texto, velocidade=0.03, newline=True):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(velocidade)
    if newline:
        print()
