class Pessoa:
    # Criando um metodo da classe Pessoa, metodos são funções criadas dentro de uma classe
    def falar(self): # O self é utilizado para referenciar o metodo a uma instancia, sendo cada instancia única
        print("Estou falando com vc")
    
    # Criando um método inicial para nossa classe
    def __init__(self, nome, idade, comendo= False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self,voce):
        if self.comendo:
            print("ta no if ")
            print(f'{self.nome}, já está comendo')
            return
        print(f'{self.nome}, Está comendo o ' , f'{voce}')
        self.comendo = True 

    def parar_de_comer(self):
        if self.comendo == False:
            print(f'{self.nome}, terminou de comer sua mãe')
            return
        else:          
            print(f'{self.nome}, vai terminar de comer')
        self.comendo = False    

    def falar(self):
        if self.comendo == True:
            print(f'{self.nome}, está comendo agora ')
            return
        else:    
            print(f'{self.nome}, pode falar') 
        self.falando = True   

    def parar_falar(self):
        if self.falando == False:
            print(f'{self.nome}, Não está falando')
            return
        else:
            print(f'{self.nome}, está terminando de falar')
        self.falando = False    

    