# Objetivo é práticar popular as listas com o metodo append() e utilizando o loop for.

# Calculando o valor da area do quadrado

#  O cálculo da área do quadrado é: Lado x lado

def Area_mesas(area):
    # Criando uma lista vazia para receber o resultado
    resultado = []
    # Loop para calcular os calculos da area, neste caso o loop percorre o valor que enviamos na lista lado
    for lado in area:
        # Criando o calculo para calcular a area do quadrado
        resultado.append(lado * lado)
    return resultado    

lado = [1, 4, 9, 20]
print(Area_mesas(lado))