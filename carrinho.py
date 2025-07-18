class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, jogo):
        self.itens.append(jogo)

    def remover(self, jogo):
        self.itens.remove(jogo)

    def total(self):
        return sum(j["preco"] for j in self.itens)

    def listar(self):
        return self.itens

    def limpar(self):
        self.itens = []