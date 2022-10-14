
import numpy as np

# Apenas para treinar o while
while True:
    opcão = 1

    print("Aperte qq numero diferente de 1 para sair")

    # Calculando a velocidade média utilizando as funções do numpy sum e len
    def velocidade_media(velocidade):
        resultado = sum(velocidade)/len(velocidade)
        resultado2 = resultado**2
        return resultado, resultado2

    def velocidade_media(velocidade):
        soma = 0
        # Aqui i assume o valor de cada dado da lista velocidade
        for i in velocidade:
            soma = soma + i
        media = soma / len(velocidade)
        return media      

    def velocidade_media(velocidade):
            count = 0
            soma = 0
            for i in velocidade:
                # aqui realizamos quantas vezes a lista é percorrida, no caso 5x por ter 5 dados nela
                count = count + 1
                soma = soma + i
            media = soma/count
            return media 

    valores = [0.389, 0.390, 0.389, 0.389, 0.389]
    print(velocidade_media(valores))
     
    opção = int(input("Deseja continuar ?")) 
    if(opção != 1):
        break    