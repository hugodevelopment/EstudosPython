# Criando listas já prontas para preencher o dicionário
nomes = ["hugo", "lucas", "adonai", "lucas", "fernanda", "marcio"]
idade = [3,4,5,6,7,9]

# Criando um dicionario vazio para ser preenchido
amigos = {}
for i in range(len(nomes)):
    # Aqui é iterado a lista preenchendo o dicionário
    amigos[nomes[i]] = idade[i]
print(amigos)

"-------------------------------------------------------------------------------------------------------------------------"

# 2º Metodo: Aqui criei uma lista e uma função para preencher a lista automaticamente
nomes1 =[]
def cadastro(nomes):
    nomes1.append(nomes)
    

# Neste for eu preencho a lista com dos nome que eu queira
amigos1 = {}
for i in range(2):
    nome = input("insira o nome: ")
    # Após o usuário escolher o nome, é chamada a função cadastro para adicionar na lista
    cadastro(nome)
    # Preencho um dicionario novo, ou até mesmo o antigo
    amigos1[nomes1[i]] = idade[i]
#printando a lista e os dicionários 
print(nomes1)
print(amigos1)     


