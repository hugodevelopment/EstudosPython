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

# Ex2: Numeros pares
def pares(x):
    print(x)
    if x == 2:
        return x
    # elif x % 2 ==0:
    #     print("É par", x)
    else:
        print("São pares ")
        pares(x - 2)

pares(10)

# Ex 3: Fatorial de um numero

# A classic example of a function that is implemented recursively 
# is the factorial function, which finds the product of all positive integers below a specified number.
# For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120). 
# To implement this recursively, notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, 
# and so on. Generally, n! = n * (n-1)!. in this case, the base case is n = 1.

print()

def factorial(n):
        return_value = 1
        for i in range(2, n + 1):
            return_value *= i
            print(return_value)
        return return_value


print(factorial(4))


