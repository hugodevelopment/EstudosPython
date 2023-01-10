# 1) What is the result of this code ?

# temos um tupla
nums = (55, 44, 33, 22)
# a função max é mais externa, que será o max entre min(nums[:2] e modulo de 42)
print(max(min(nums[:2]), abs(-42)))


# 2 Drag and drop from the options below to print only the items in the set "a" that are not in the set "b".
  
a = {1,4,5}
b = {9,5,1}

print(a - b)


# 3 Fill in the blanks to create a list of numbers multiplied by 10 in the range of 5 to 9.

lista = [i *10  for i in range(5,9)]
print(lista)



def contando_letras(nome, letra):
    count = 0
    for i in nome:
        if i == letra:
            count += 1            
    print(letra," tem ", count)       
    return count

print(contando_letras("hugoo", "o"))    


# Treinando iteração com dicionarios: Minha ideia é iterar automaticamente dicionarios para adicionar valores

# 1º Criando a função para receber nome e nota
def dicio(keys, i, values):
    alunos = {}
    alunos[keys[i]] = values[i]
    return alunos

# 2º criando um for para adicionar os valores:
for i in range(2):
    nome = input("insira um nome:")
    nota = input("Insira a nota")
    
