'''
link: https://www.computersciencemaster.com.br/exercicio-sistema-de-lanchonete/
'''
class Comida:
    def __init__(self, preco, validade, peso, nome):
        self.preco = preco
        self.validade = validade
        self.peso = peso
        self.nome = nome
        pass

class Pizza(Comida):
    def __init__(self, preco, validade, peso, nome):
        super().__init__(preco, validade, peso, nome)
    pass

class Lanches(Comida):
    def __init__(self, preco, validade, peso, nome):
        super().__init__(preco, validade, peso, nome)
    pass

class Salgadinhos(Comida):
    def __init__(self, preco, validade, peso, nome):
        super().__init__(preco, validade, peso, nome)
    pass

class Pedido:
    def __init__(self, nome_cliente, itens, taxa_servico = 0.10):
        self.nome_cliente = nome_cliente
        self.itens = itens
        self.taxa_servico = taxa_servico
        pass
    
    def adiciona(self, item):
        self.lista = []
        self.lista.append(self.itens)
        self.lista.append(item)
        return self.lista

    def mostra(self):
        for i in self.lista:
            print(
            f'Seu pedido tem {i.nome}'
        )


    def recebe():
        pass

    def troco():
        pass


class Nota_fiscal(Pedido):
    #mostrar o nome do cliente
    #mostrar o nome e o valor de tudo o que foi pedido
    
    pass

pedido = Pizza(50, 'ontem', 1, 'Marguerita')
print(pedido.nome)

pedido1 = Pedido('Felipe', pedido)
pedido1.adiciona(Salgadinhos(1.5,'hoje',50,'coxinha'))
pedido1.mostra()