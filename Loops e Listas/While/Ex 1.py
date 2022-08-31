
# Exercicio: Faça um programa que peça um número maior que 1 ao usuário. Em
# seguida, imprima todos os números, de 1 até o número que o usuário informou

#Como resolver: Neste caso, iremos usar o loop while, já que não temos um condição pré-definido para finalizar o loop

# O usuário irá escolher um número para começar, neste caso escolhemos uma variável inteira
numero_user = int(input("Digite um número maior que 1:"))
print("O número escolhido é ", numero_user)

# Variável para contabilizar a contagem
count = 0

# Criar um loop while para imprimir a contagem de números até o número que o usuário escolheu
while count < numero_user:
    print(count) # A contagem começará do 0
    count += 1 # é equivalente a count = count + 1