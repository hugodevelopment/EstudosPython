"""
Recursion is a very important concept in functional programming.
The fundamental part of recursion is self-reference -- functions calling themselves. 
It is used to solve problems that can be broken up into easier sub-problems of the same type.
"""

# Ex1 : Uma função regressiva
def countdown(x):
    print(x)
    # valor para sair do loop da função
    if x==0: 
        return 
    else:
        # Aqui acontece a recursão
        countdown(x-1) 

countdown(10)   

# # Ex2: Numeros pares
# def pares(x):
#     print(x)
#     if x == 2:
#         return x
#     else:
#         print("São pares ")
#         pares(x - 2)

# pares(10)

# Ex 3: Fatorial de um numero

# A classic example of a function that is implemented recursively 
# is the factorial function, which finds the product of all positive integers below a specified number.
# For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120). 
# To implement this recursively, notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, 
# and so on. Generally, n! = n * (n-1)!. in this case, the base case is n = 1.

print()

# # Função de fatorial sem recursão, apenas com for. Calcula de forma crescente
# def factorial(n):
#         return_value = 1
#         # O for irá percorer de 2 até o número escolhido, nesse caso 4 
#         for i in range(2, n + 1): 
#             print("valor de i", i)
#             return_value *= i # Aqui é feito o cálculo da recursão, recebendo cada valor e multiplciando por i
#             print(return_value)
#         return return_value
# print(factorial(4))


# Aqui podemos ver que é decrescente, do maior(4) para o menor(1)
# def fatorial_recursão(n):
#     print(n)
#     # A função recebe n e verifica se é igual a 1
#     if n == 1:
#         return 1
#     # Senão n não for 1, então faça a expressão abaixo 
#     else:
#         return n * fatorial_recursão(n-1)

# print(fatorial_recursão(4))             


# # Com lambda:
# fatorial_lambda = lambda x: 1 if x == 1 else  x * fatorial_lambda(x-1)
# print(fatorial_lambda(4))


# Sequencia de fibonnaci com recursão
def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
        
def menu():
    n = int(input('Exibir ate o termo (maior que 2): '))

    for i in range(1,i+1):
        print(fibo(i))
    
menu()

