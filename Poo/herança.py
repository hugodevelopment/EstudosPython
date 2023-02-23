# Inheritance provides a way to share functionality between classes.
# Imagine several classes, Cat, Dog, Rabbit and so on. 
# Although they may differ in some ways (only Dog might have the method bark),
#  they are likely to be similar in others (all having the attributes color and name).

# Exemplo, vou criar uma classe dragonball, onde os demais persnagens irão herdar atributos básicos.

# Essa é uma superclasse
class DragonBall():
    def __init__ (self, nome, idade, nivel_poder,raça,mestre):
        self.nome = nome
        self.idade = idade
        self.nivel_poder = nivel_poder
        self.raça = raça
        self.mestre = mestre

# Essa é uma subclasse que herda atributos da classe Dragobnaball
class Ataque(DragonBall):
    def ataque(self,golpe):
        print(self.nome,"Meu golpe é ",golpe) 

Personagem1 = Ataque("Goku", 15, 200, "Sayajin", "Kame")
print(Personagem1.nome)
print(Personagem1.nivel_poder)
Personagem1.ataque("Kamehamehaaaa")

personagem2 = Ataque("Vegeta", 17, 210, "Sayajin", "nao tem")
personagem2.ataque("Final Flash")
