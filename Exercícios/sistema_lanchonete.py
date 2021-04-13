'''
link: https://www.computersciencemaster.com.br/exercicio-sistema-de-lanchonete/
'''
class Comida:
    def __init__(self, preco, validade, peso):
        self.preco = preco
        self.validade = validade
        self.peso = peso
        pass

class Pizza(Comida):
    pass

class Lanches(Comida):
    pass

class Salgadinhos(Comida):
    pass

class Pedido:
    def __init__(self, nome_cliente, itens, taxa_servico):
        self.nome_cliente = nome_cliente
        self.itens = itens
        self.taxa_servico = taxa_servico
        pass
    pass

def recebe():
    pass

def troco():
    pass

class Nota_fiscal:
    pass