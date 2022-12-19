# Slicing is yet another super practical aspect of Python. 
# It makes accessing strings, lists and tuples partially very effortless.

# Syntax
# 1) Follow the syntax notation [start:end:step]

# 2) If start is not given it will start from 0 (zero)

# 3) If end is not given it will go all the way to the end

# 4) If step is not given, steps will increase by 1

# https://holypython.com/beginner-python-lessons/lesson-17-slicing/

# Exemplo 1

lista = [1,5,6,7,8,9]
# neste caso a variavel a receberá os numeros que correspondem a posição 1 e 3 da lista, já que o ultimo número(4) não conta
a= lista[1:5]
print(a)
print("4º posição da lista:", lista[4])


#Exemplo 2 com a função range
lista = list(range(1,15,2))  # a função range cria uma lista que vai de 1 a 15(não-incluindo) de 2 em 2 números
print(lista)
# Neste caso o slicing vai do 2º termo ao 5º de 2 em 2
a = lista[1:6:2]
print(a)


#Exemplo 3 omitindo os passos
lista = list(range(10))
print(lista)
# Neste caso eu estou omitindo onde se deve parar, então iremos até o final da lista começando do 2º termo
a = lista[1::]
# Aqui iremos do começo, começando do 1º termo e indo até o final de 2 em 2 números
b = lista[::2]
print(b)
