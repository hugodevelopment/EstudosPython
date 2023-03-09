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
        self.horas_trabalhadas = 0
        self.salario = 0

    def horas_trabalhos(self):
        self.horas_trabalhadas =+ 1

    def calcular_salário(self):
        self.salario = self.horas_trabalhadas * self.valor_hora_trabalhada        


# O problema desta classe é que ela pode alterar o salario de um cliente de modo arbitrario, 
# sem precisar utilizar os metodos criadas na classe

funcionario1 = funcionario("Hugo", "estudante" , 3)
# coloquei 1000 reais de maluco
salario = funcionario1.salario = 1000


# Em Python, existe uma convenção de que dados ou métodos cujo nome começa com 
# _ (dois _underscores) não deveriam ser acessados fora da classe
class funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        # Posso criar variaves mesmo fora do init(Revisar)
        self.__horas_trabalhadas = 0
        self.__salario  = 0

    def horas_trabalhos(self):
        self.horas_trabalhadas =+ 1

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada

# Isso já é um avanço, pois sinaliza a clientes da classe que as variáveis horas_trabalhadas e 
# salario não devem ser alteradas arbritrariamente.

funcionario1 = funcionario("Hugo", "estudante" , 3)
# Ainda é possivel alterar, mesmo com as indicações
funcionario1.__salario = 2000
print(funcionario1.__salario)


# Outra classe agora com encapsulamento
class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__salario = 0
        self.__horas_trabalhadas = 0

    @property
    def salario(self): 
        return self.__salario
    
    # Caso o usario tente alterar o salario não será possível
    @salario.setter
    def salario(self, novo_salario): 
        raise ValueError("Impossivel alterar salario diretamente. Use a funcao calcula_salario().")

    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada
        return self.__salario


# revisar instanciar
funcionario1 = Funcionario("Hugo", "estagio" , 3)
# Agora não será mais possível alterar
# funcionario1.salario = 3000
# print(funcionario1.salario)       
funcionario1.registra_hora_trabalhada()
salario = funcionario1.calcula_salario()
print(salario)

      