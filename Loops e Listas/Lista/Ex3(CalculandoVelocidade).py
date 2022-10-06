
import numpy as np

while True:
    opcão = 1

    print("Aperte qq numero diferente de 1 para sair")

    # Calculando a velocidade média utilizando as funções do numpy sum e len
    
    def velocidade_media(velocidade):
        resultado = sum(velocidade)/len(velocidade)
        resultado2 = resultado**2
        return resultado, resultado2

    def velocidade_media(velocidade):
        for valores in velocidade:
            soma = soma + valores
        media = soma / len(velocidade)
        return media      

    def velocidade_media(velocidade):
        count = 0
        soma = 0
        for valores in velocidade:
            count = count + 1
            soma = soma + valores
        media = soma/ count
        return media 

    valores = [0.389, 0.390, 0.389, 0.389, 0.389]
    print(velocidade_media(valores))
     
    opção = int(input("Deseja continuar ?")) 
    if(opção != 1):
        break    