nomes = ["hugo", "lucas", "adonai", "lucas", "fernanda", "marcio"]
idade = [3,4,5,6,7,9]

amigos = {}
for i in range(len(nomes)):
    amigos[nomes[i]] = idade[i]
print(amigos)


nomes1 =[]
def cadastro(nomes):
    nomes1.append(nomes)
    print(nomes1)

for i in range(2):
    nome = input("insira o nome: ")
    cadastro(nome) 


amigos = {}
for i in range(len(nomes)):
    amigos[nomes1[i]] = idade[i]
print(amigos)           

# dicts = {}

# keys = [10, 12, 14, 16]
# values = ["A", "B", "C", "D"]

# for i in range(len(keys)):
#     dicts[keys[i]] = values[i]
# print(dicts)    