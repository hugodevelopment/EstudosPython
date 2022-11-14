#  for loops repeat a portion of code for a set of values.
#  for loops work slightly differently than they do in languages such as JavaScript or C.
#  A for loop sets the iterator variable to each value in a provided list, array, 
# or string and repeats the code in the body of the for loop for each value of the iterator variable.

# Ex 1
lista = [1,3,4,5,6,7,8]
for i in lista:
    print("printando cada valor da lista",i)

# We can include more complex logic in the body of a for loop as well. 
# Ex 2:
for i in lista:
 x = i**2 - (i-1)*(i+1)
#  print(x, end= ", ")

#  Criando funções para realizar o mesmo calculo
def sempre_1(x):
    return x**2 - (x-1)*(x+1)

# Iterando a lista com a função
for i in lista:
    sempre_1(i)
    # print(sempre_1(i))

# Acessando elementos:
# How do I access the index while iterating over a sequence with a for loop?

# item #1 = 8
# item #2 = 23
# item #3 = 45

# Acessando itens com enemurate para criar um indez
list = [8, 23, 45]
for index, i in enumerate(list):
    print(index, i)