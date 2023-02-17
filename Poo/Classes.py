# The __init__ method is the most important method in a class.
# This is called when an instance (object) of the class is created, 
# using the class name as a function.
# All methods must have self as their first parameter, 
# although it isn't explicitly passed, 
# Python adds the self argument to the list for you; 
# you do not need to include it when you call the methods. Within a method definition, 
# self refers to the instance calling the method.

# Criando a classe jogador
class Player:
    def __init__(self,nome,level):
        self.nome = nome
        self.level = level
    
    def intro(self):
        print(f'{self.nome}, seu level é ' f'{self.level}')

# Criando uma instancia da classe, ou seja, um objeto
Jogador1 = Player("Hugo", 25)
jogador2 = Player("Lucas", 23)

# Chamando o metodo para cada jogador
Jogador1.intro()
jogador2.intro()