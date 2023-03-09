# Encapsulamento é um dos pilares da programação orientada a objetos, 
# segundo o qual procuramos esconder de clientes (usuários de uma classe) 
# Todas as informação que não são necessárias ao uso da classe.


# Por exemplo, suponha que precisássemos criar uma classe para armazenar informações de funcionários de uma empresa, 
# como ilustrado no exemplo abaixo.

class funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        # Posso criar variaves mesmo fora do init
        self.valor_hora_trabalhada = 0
        self.salario = 0