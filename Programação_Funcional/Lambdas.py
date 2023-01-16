# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.


# x é a função anonima que não precisamos definir como def; 
# a é o parametro que será utilizado na função
x = lambda a: a + 15
print(x(5))

# Fazendo com mais argumentos, mesma ideia da anterior
x = lambda a,b,c: a + b + c
print(x(10,5,20))


# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Ex 1 - Sem utilziar a funçao lambda iremos fazer normalmente
def calcular_imposto(tax):
    return tax * 0.5
print("O imposto é sem lambda", calcular_imposto(1000))

# Ex 2: Utilizando o lambda não foi necessário utilizar o def
# fizemos tudo em uma linha e como se colocar o retorno na propria função
calcular_imposto = lambda tax: tax * 0.5
print("com lambda ", calcular_imposto(1000))


# On each iteration inside the list comprehension, 
# we are creating a new lambda function with default argument of x (where x is the current item in the iteration). 
# Later, inside the for loop, 
# we are calling the same function object having the default argument using imposto() 
# and getting the desired value. Thus, nova_lista stores the list of lambda function objects

# Aqui criamos uma lista onde para cada iteração a função lambda é chamada, neste cado i se torna x em cada iteração
nova_lista = [lambda i = x: i * 0.5  for x in range(50,60)]
imposto_lista = []
for imposto in nova_lista:
    print(imposto())
 
 
# No exemplo acima, criamos uma função lambda que classifica cada sublista da lista fornecida. 
# Em seguida, essa lista é passada como parâmetro para a segunda função lambda, 
# que retorna o elemento n-2 da lista classificada,  onde n é o comprimento da sublista.
List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]

# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)

# Get the second largest element
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)


