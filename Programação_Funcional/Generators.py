# Generator-Function: A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. 
# If the body of a def contains yield, the function automatically becomes a generator function. 

# Vamos fazer um função regressiva:

def countdown():
    i = int(input("escolha um numero"))
    while i > 0:
        yield i
        i -= 1


for i in countdown():
    print(i)