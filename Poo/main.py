from pessoa import Pessoa

# Hhama-se instância de uma classe, 
# Um objeto cujo comportamento e estado são definidos pela classe. 
# O uso da palavra "Instância" pode ter sido inspirado no inglês; 
# tal palavra significa "caso" ou "exemplo" em inglês


# vamos instanciar a classe pessoa, criando objetos
# pessoa1= Pessoa()
# pessoa2= Pessoa()

# Criando atributos para as pessoas de uma maneira menos eficaz
# pessoa1.nome = "Hugo"
# pessoa2.nome = "Lucas"
# print(pessoa1.nome)
# print(pessoa2.nome)

# Agora vamos criar de uma maneira melhor, utilizando a classe Pessoas
pessoa1 = Pessoa("Hugo", 26)
pessoa2 = Pessoa("Marcio",25)
pessoa1.comer("Maça")
pessoa1.comer("Pera")
# pessoa1.parar_de_comer()
# pessoa1.falar("Henrique")
# pessoa1.falar("Marcio")