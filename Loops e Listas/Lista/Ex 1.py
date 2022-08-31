"""Exercício de Listas em Python
Crie um programa em Python que peça seu nome, sua idade, sua altura, seu peso e True se for casado ou False para solteiro.
Em seguida, ele deve armazenar todas essas informações numa lista chamada eu. Por fim, imprima essa lista na tela.""" 

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade :"))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

civil = input("Digite 1 para casado e 2 para solteiro: ")

if civil == 1:
   civil = True
else:
    civil = False    

eu = [nome,idade, altura, peso, civil]
print(eu)