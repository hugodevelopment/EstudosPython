def conta_palavras(frase):
    # Identifica as palavras
    palavra = ''
    palavras = [''] * len(frase)
    j = 0
    for char in frase:
        if char == ' ':
            j += 1
        else:
            palavras[j] += char

    # Identifica as palavras únicas
    palavras_unicas = [''] * len(palavras)
    k = 0
    for palavra in palavras:
        if palavra not in palavras_unicas:
            palavras_unicas[k] = palavra
            k += 1

    # Conta quantas vezes cada palavra aparece
    contagem = [0] * len(palavras_unicas)
    for i in range(k):
        for palavra in palavras:
            if palavra == palavras_unicas[i]:
                contagem[i] += 1

    # Imprime a contagem de cada palavra
    for i in range(k):
        print('A palavra "' + palavras_unicas[i] + '" aparece ' + str(contagem[i]) + ' vez(es) na frase.')

# Testa a função
conta_palavras('o que é o que é')
