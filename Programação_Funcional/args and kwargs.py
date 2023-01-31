# In this article, 
# we'll discuss *args and **kwargs in Python along with their uses and some examples.

# Nesta função soma, utilizei o *args para enviar mais parametros de uma vez a função
def soma(*x):
    print(x)
    total = 0 
    for i in x:
        total += i
    return total    

# Quando utilizamos o *args, uma tupla é criada dentro da função para realizar as operações
print(soma(2,3,4))



# **kwargs allows us to pass a variable number of keyword arguments to a Python function. In the function, we use the double-asterisk (**) 
# before the parameter name to denote this type of argument.

def total_fruits(**kwargs):
    # Kwargs retorna um dicionário
    print(kwargs, type(kwargs))
total_fruits(banana=5, mango=7, apple=8)


# Melhorando a função que recebe o dicionário com kwargs
def total_fruits(**fruits):
    total = 0
    for i in fruits.values():
        if i > 10:
            print("Muito caro hein", i)
        total += i       
    return total 

print(total_fruits(laranja =10, abacaxi=13, limão=5))       

# The given code defined a function called my_min(), which takes two arguments and returns the smaller one.
# You need to improve the function, so that it can take any number of variables, so that the function call works.

def my_min(*x):
    menor = 500
    print(x)
    for i in x:
        if i < menor:
            menor = i
    return menor


print(my_min(8, 13, 4, 42, 120, 7))