def conta_palavras(frase):
    # Identifica as palavras únicas
    palavra = ''
    palavras = []
    for char in frase:
        if char == ' ':
            palavras.append(palavra)
            palavra = ''
        else:
            palavra += char
    palavras.append(palavra)  # Adiciona a última palavra

    palavras_unicas = []
    for palavra in palavras:
        if palavra not in palavras_unicas:
            palavras_unicas.append(palavra)
    
    # Conta quantas vezes cada palavra aparece
    contagem = []
    for palavra_unica in palavras_unicas:
        cont = 0
        for palavra in palavras:
            if palavra == palavra_unica:
                cont += 1
        contagem.append(cont)
    
    # Imprime a contagem de cada palavra
    for i in range(len(palavras_unicas)):
        print('A palavra "' + palavras_unicas[i] + '" aparece ' + str(contagem[i]) + ' vez(es) na frase.')

# Testa a função
conta_palavras('o que é o que é')
