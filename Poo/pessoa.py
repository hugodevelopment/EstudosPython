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
        # self.comendo = True 


    def parar_de_comer(self):
        if self.comendo == True:
            print("Vou parar de comer ")
        else:        
            print("Termimando...")
        self.comendo = False    


    def falar(self,voce):
        if self.falando:
            print(f'{self.nome}, já está conversando ')
            return
        print(f'{self.nome}, esta falando com', f'{voce}') 
        self.falando = True   

    