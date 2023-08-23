class Fila:
    def __init__(self):
        self.dados = []

    def __str__(self):
        return self.dados

    def is_empty(self):
        return not self.dados

    def size(self):
        return len(self.dados)

    def enfileirar(self, valor):
        self.dados.append(valor)

    def desenfileirar(self):
        return self.dados.pop(0)

    def get_inicio(self):
        return self.dados[0]