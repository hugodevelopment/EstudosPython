# Ex: Crie um joguinho para o usuario advinhar um numero entre posibilidades aleatórias
# Como resolver: Vamos criar uma variável para contar as tentativas, além de um loop para finalizar quando o numero do usuario for igual ao numero sorteado

import random

numero_magico = random.randint(0,100)
print(numero_magico)


while True:
        numero_user = int(input("Digite um número para brincar"))
        if numero_user == numero_magico:
            print("Você acertou, parabéns")
            break
        opcao = int(input("Digite 1 para sair ou qualquer para continuar"))
        if opcao == 1:
            break

        