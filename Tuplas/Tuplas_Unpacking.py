# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
amigos = ("Adonai", "Lucas", "Lucas", "Fernanda", "Marcio")
print(amigos)

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
nome1, nome2, nome3, nome4, nome5 = amigos
# Neste caso a variável nome1 recebe o primeiro indice da tupla amigos
print(nome1)

# Using Asterisk*
# If the number of variables is less than the number of values, 
# you can add an * to the variable name and the values will be assigned to the variable as a list:
nome1, nome2, *nome3  = amigos
# Nome3 recebera os proximos nomes como uma lista
print(nome3)

'----------------------------------------------------------------------------------------------------------'
# Tuples can be used to output multiple values from a function.
# You need to make a function called calc(), that will take the side length of a square as its argument and return the perimeter and area using a tuple.
# The perimeter is the sum of all sides, while the area is the square of the side length.

# Então neste caso o retorno da função deve ser uma tupla com os valores de area e perimetro 
def calc(x):
    # criando a tupla
    tupla = (x*4, x**2)
    return tupla

# Utilizando o unpacking com os valores
peri, area = calc(3)
for i in calc(3):
    print("valores da tupla", i)   