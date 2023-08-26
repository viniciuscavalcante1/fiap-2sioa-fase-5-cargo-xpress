from utils.Fila import Fila
from utils.Pilha import Pilha
from utils.funcoes_mercadorias import gerar_carga, \
    get_status_encarregamento, \
    carregar_mercadoria, \
    print_letra_por_letra

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

for minuto in range(100):
    print_letra_por_letra("\n######################################################################################",
                          0.005)
    print_letra_por_letra(f"# [HORÁRIO] 20h{minuto} ###############################################################"
                          f"######", 0.005)
    print_letra_por_letra("######################################################################################\n",
                          0.005)
    if minuto == 0:
        fila_total_mercadorias = gerar_carga(total_mercadorias)
        print_letra_por_letra(f"[20h{minuto} - INÍCIO: VAN CHEGOU]\n"
                              f"\tA van da empresa de logística chegou.\n"
                              f"\t{total_mercadorias} cargas aleatórias foram geradas...")
        print_letra_por_letra(f"\n\tVamos inserir as mercadorias na fila de carregamento.\n"
                              f"\tPara agilizar, vamos preparar {fila_inicial} mercadorias de uma só vez "
                              f"inicialmente.\n"
                              f"\tA partir daí, 1 nova mercadoria será inserida a cada dois minutos.\n"
                              f"\tO tempo total para carregar cada mercadoria será de {minutos_carregar_mercadoria} "
                              f"minutos.\n")
        for i in range(fila_inicial):
            fila_carregar_mercadorias.enfileirar(fila_total_mercadorias.desenfileirar())
            fila_carregar_mercadorias.dados[i].set_horario_fila_de_carga(f"20h{minuto}")
            mercadorias_inseridas_na_fila += 1
            print_letra_por_letra(
                f"\n[20h{minuto} - MERCADORIA ADICIONADA À FILA DE CARREGAMENTO:"
                f" {fila_carregar_mercadorias.dados[i]}]\n"
                f"\tRestam {total_mercadorias - mercadorias_inseridas_na_fila} mercadorias para serem"
                f" adicionadas à fila.\n"
                f"\tItens na fila no momento: {fila_carregar_mercadorias.size()}\n")
    if ajudante is None:
        print_letra_por_letra("\n[PERGUNTA]\n"
                              "\tBom, já adicionamos três mercadorias à fila! Teremos um ajudante para nos"
                              " auxiliar a carregá-las na van?\n"
                              "\tInsira 'S' para SIM ou 'N' para não.")
        resposta_ajudante = input("\tRESPOSTA: ").upper()
        while resposta_ajudante not in ('S', 'N'):
            print_letra_por_letra("\t\t[ERRO] Por favor, insira uma resposta válida ('S' para SIM ou 'N' para não).")
            resposta_ajudante = input("\t\tResposta: ").upper()
        if resposta_ajudante == 'S':
            ajudante = True
            print_letra_por_letra("\n[TEMOS AJUDANTE!]\n"
                                  "\tÓtimo! Vai ser muito mais rápido com um ajudante.\n"
                                  "\tVamos colocar mais alguns produtos na fila, e aí, partiu carregar pra van!")
        else:
            ajudante = False
            print_letra_por_letra("\n[NÃO TEMOS AJUDANTE :(]\n"
                                  "\tBeleza! Vamos à guerra sem ajuda, então.\n"
                                  "\tSó mais uns minutos e já iniciaremos.")

    if minuto % 2 == 0 and mercadorias_inseridas_na_fila < total_mercadorias and minuto > 0:
        fila_carregar_mercadorias.enfileirar(fila_total_mercadorias.desenfileirar())
        fila_carregar_mercadorias.dados[-1].set_horario_fila_de_carga(f"20h{minuto}")
        mercadorias_inseridas_na_fila += 1
        print_letra_por_letra(
            f"\n[20h{minuto} - MERCADORIA ADICIONADA À FILA DE CARREGAMENTO: {fila_carregar_mercadorias.dados[-1]}]\n"
            f"\tRestam {total_mercadorias - mercadorias_inseridas_na_fila} mercadorias para serem adicionadas à fila.\n"
            f"\tItens na fila no momento: {fila_carregar_mercadorias.size()}.\n")

    if minuto == 10:
        print_letra_por_letra(
            f"Bom, já se passaram 10 minutos! Agora são 20h{minuto} e já temos {mercadorias_inseridas_na_fila}"
            f" mercadorias na fila, uma quantidade considerável! Vamos começar a carregar!")
        if ajudante is True:
            print_letra_por_letra("Como temos um ajudante para nos auxiliar, podemos carregar dois produtos de uma só "
                                  "vez!")
        else:
            print_letra_por_letra("Não temos ajudante, então vamos carregar uma mercadoria de cada vez.")
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
                print_letra_por_letra(
                    f"\n[20h{minuto} - CARREGAMENTO DE MERCADORIA CONCLUÍDO: {carga}]\n"
                    f"\tA mercadoria {carga} entrou na fila de carga às {carga.get_horario_fila_de_carga()} e "
                    f"teve seu carregamento finalizado às {carga.get_horario_carregada()}, com "
                    f"um tempo de espera total de {carga.get_tempo_de_espera()} minutos.\n")
        if len(dic_mercadorias_sendo_carregadas) == 0:
            if fila_carregar_mercadorias.size() == 0:
                print_letra_por_letra("\n[FIM! CARREGAMOS TODOS OS PRODUTOS!]")
                print_letra_por_letra("\n[RESUMO]")
                print_letra_por_letra("\n[Horário em que a mercadoria foi inserida na fila | Horário em que "
                                      "terminou de ser carregada | Tempo de espera | Nome e ID]")
                for mercadoria in pilha_mercadorias_van.dados:
                    print_letra_por_letra(f"{mercadoria.get_horario_fila_de_carga()} | ",
                                          newline=False)
                    print_letra_por_letra(f"{mercadoria.get_horario_carregada()} | ", newline=False)
                    print_letra_por_letra(f"{mercadoria.get_tempo_de_espera()} minutos | ", newline=False)
                    print_letra_por_letra(f"{mercadoria}", newline=False)
                    print()
                break
            else:
                carregar_mercadoria(fila_carregar_merc=fila_carregar_mercadorias,
                                    horario=minuto,
                                    dic=dic_mercadorias_sendo_carregadas,
                                    pilha_merc_van=pilha_mercadorias_van,
                                    tempo_para_carregar=minutos_carregar_mercadoria,
                                    ajuda=ajudante)
