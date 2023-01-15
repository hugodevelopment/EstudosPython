# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Example:

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
frutas = ["banana", "maça", "pera", "pessego", "kiwi", "mango"]

nova_lista = []

# função appendar a lista caso a fruta tenha a
def fruta(x):
    # se a fruta tem a no nome, vamos preencher na nova lista
    if "a" in x:
        nova_lista.append(x)
    else:
        pass

# Without list comprehension you will have to write a for statement with a conditional test inside:
for i in frutas:
    fruta(i)
print("sem compressão da lista", nova_lista)    

#Utilziando list comprenhesion: 
nova_lista2 = [i for i in frutas if "a" in i]
print("com compressão da lista", nova_lista2)

# Sintax:
# newlist = [expression for item in iterable if condition == True]

# Exemplo para as frutas que não tem a 
nova_lista3 = [i for i in frutas if "a" not in i]
print(nova_lista3)

Lista_até_5 = [i for i in range(10) if i < 5]
print(Lista_até_5)


valor = [1000, 2000, 5000, 4000, 6000]
desconto = 200

def desconto_preço(x):
    return x - desconto

produtos = [desconto_preço(i) for i in valor]
print(produtos)