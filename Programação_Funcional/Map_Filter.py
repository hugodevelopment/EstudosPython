# Map() function returns a map object(which is an iterator) 
# of the results after applying the given function to each item of a given iterable (list, tuple etc.)

# Syntax :

# map(fun, iter)
# Parameters :
# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.

# Criamos uma função para adicionar 5 para cada numero da lista que iremos passar como parametros
def add_5(x):
    return x + 5

numeros = [1,3,4,5,6,7]
# Transformamos o resultado map em uma lista
resultado = list(map(add_5,numeros))
print("sem lambda ", resultado)

# Vamos fazer utilizando lambda
resultado = list(map(lambda x: x + 5, numeros))
print("com lambda", resultado)


# Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

# Soma cada elemento da lista entre si, como 1 + 4, 2 + 5 e 3 + 6
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))


# Exercicse Sololearn
# You work on a payroll program.
# Given a list of salaries, you need to take the bonus everybody is getting as input and increase all the salaries by that amount.
# Output the resulting list.

salaries = [2000, 1800, 3100, 4400, 1500]
bonus = 20

print(list(map(lambda x: x + bonus,salaries)))


"-------------------------------------------------------------------------------------------------------------------------------"

# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
# syntax:
# filter(function, sequence)

# Funções para criar a condição de aceitar apenas vogais
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False
  
  
# sequence
sequence = ['g', 'e', 'a', 'j', 'k', 's', 'p', 'r']
  
# using filter function, enviando como parametros a função e a sequencia que queremos testar
filtered = filter(fun, sequence)

# Printando as letrais que são vogais na sequencia  
print('The filtered letters are:')
for s in filtered:
    print(s)


numbers = [-2, -1, 0, 1, 2]

def numeros_positivos(x):
    positivos = []
    for i in x: 
        if i > 0:
            positivos.append(i)      
    return positivos 

print("Com função ",numeros_positivos(numbers))


# Utilizando filter fica mais simples, veremos:
numbers = [-2, -1, 0, 1, 2]

# Using a lambda function with filter
positive_numbers = filter(lambda n: n > 0, numbers)
print("Com filter e lambda", list(positive_numbers))


