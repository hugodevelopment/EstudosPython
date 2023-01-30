# In this article, 
# we'll discuss *args and **kwargs in Python along with their uses and some examples.

# Nesta função soma, utilizei o *args para enviar mais parametros de uma vez a função
def soma(*x):
    total = 0 
    for i in x:
        total += i
    return total    

# Quando utilizamos o *args, uma tupla é criada dentro da função para realizar as operações
print(soma(2,3,4))



# **kwargs allows us to pass a variable number of keyword arguments to a Python function. In the function, we use the double-asterisk (**) 
# before the parameter name to denote this type of argument.