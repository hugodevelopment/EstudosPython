# Exercicios do site Holy Python 

# 1º Write a while loop that adds all the numbers up to 100 (inclusive).

# Neste caso nos precisamos criar um loop para contar até 100, com o número 100 incluso
contador = 0
total = 0

while (contador <= 100):
    total = total + contador
    contador += 1
print(total)

# ---------------------------------------- Ex 2 -------------------------------------------

# Using while loop, if statement and str() function; iterate through the list and if there is a 100, print it with its index number. i.e.: 
# "There is a 100 at index no: 5"


lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
#Type your code here.

i = 0
while(i < len(lst)):
    if(lst[i] == 100):
        print("There is a 100 at index no:", i)
    i+=1
