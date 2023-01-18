# Generator-Function: A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. 
# If the body of a def contains yield, the function automatically becomes a generator function. 

# Vamos fazer um função regressiva que diminuindo a de 1 em  1
def countdown():
    i = int(input("escolha um numero"))
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)


# Preenchendo uma lista até 100 sem gerador
def lista_100():
    lista = []
    for i in range(100):
        lista.append(i)
    return lista 

# Transformar uma função em uma variável
l = lista_100()

# Percorre a lista crianda na função lista_100()
for v in l:
    print(v)
 
 