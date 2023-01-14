# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Example:

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:
frutas = ["banana", "maça", "pera", "pessego", "kiwi", "mango"]

nova_lista = []

# função appendar a lista caso a fruta tenha a
def fruta(x):
    # se a fruta tem a no nome, vamos preencher na nova lista
    if "a" in x:
        nova_lista.append(x)
    else:
        pass

for i in frutas:
    fruta(i)
print(nova_lista)    

    
    
