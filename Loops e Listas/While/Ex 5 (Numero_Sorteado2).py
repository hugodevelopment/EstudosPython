import random

numero_magico = 55


while True:
        numero_user = int(input("Digite um número para brincar"))
        if numero_user == numero_magico:
            print("Você acertou, parabéns")
            break
        elif numero_user == 54 or numero_user == 56:
            print("Está perto")
        opcao = int(input("Digite 1 para sair ou qualquer para continuar"))
        if opcao == 1:
            break