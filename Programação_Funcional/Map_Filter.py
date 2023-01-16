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
bonus = int(input())

print(list(map(lambda x: x + bonus,salaries)))
