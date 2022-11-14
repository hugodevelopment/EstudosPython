
def dobro(lista):
    # Criando uma lista vazia para receber o resultado
    resultado = []
    # Loop para calcular a lista de numeros
    for x in lista:
        # Criando o calculo para elevar os números ao quadrado
        resultado.append(x**2)
    return resultado    

lista = [1, 4, 9, 20]
print(dobro(lista))


