# def conta_vogais(string):
#     string = string.lower() # para que a comparação não seja sensível a maiuscula/minuscula
#     result = {}
#     vogais = 'aeiou'
#     for i in vogais:
#         if i in string:
#             result[i] = string.count(i)
#     return result

# print(conta_vogais('olaaa'))

def conta_vogais(string):
    string = string.lower() # para que a comparação não seja sensível a maiuscula/minuscula
    sao_vogais = []
    vogais = 'aeiou'
    for i in vogais:
        if i in string:
            sao_vogais.append(i)
    return sao_vogais

print(conta_vogais('olaaa'))