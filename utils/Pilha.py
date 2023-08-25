class Pilha:
    def __init__(self):
        self.dados = []

    def __str__(self):
        return str(self.dados)

    def empilhar(self, valor):
        self.dados.append(valor)

    def desempilhar(self):
        return self.dados.pop()

    def e_vazia(self):
        return not self.dados

    def tamanho(self):
        return len(self.dados)