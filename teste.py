import time

hora_chegada = 20
minuto_chegada = 0
fila = []
mercadorias_na_fila = 0
tempo_espera_total = 0

# Passo 1: Calcular X (tempo de carregamento)
# Substitua o valor de RM pelo RM de um colega
rm_colega = 12345
x = (rm_colega % 3) + 1

# Passo 3: Loop principal
while len(fila) > 0 or mercadorias_na_fila > 0:
    time.sleep(1)  # Simula o avanço de 1 minuto
    minuto_chegada += 1

    # Passo 4: Adicionar mercadorias à fila
    if minuto_chegada % 2 == 0 and mercadorias_na_fila < 15:
        fila.append(minuto_chegada)
        mercadorias_na_fila += 1

    # Passo 5: Carregar mercadorias
    if minuto_chegada >= 10 and fila:
        tempo_espera = minuto_chegada - fila[0] + x
        tempo_espera_total += tempo_espera
        fila.pop(0)
        mercadorias_na_fila -= 1

# Passo 7: Exibir resultados
print("Tempo total de espera:", tempo_espera_total, "minutos")