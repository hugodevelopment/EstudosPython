
# 1º Criar uma lista com dos valores que iremos analisar se estão dentro do intervalo
# 2º Utilizar o for para percorrer a lista e analisar quais dos valores estarão dentor do intervalo
# 3º Utilizar o if para verificar a condição 

dados = [8.28,8.22,8.29,8.25,8.26,8.26,8.26,8.23,8.30,8.27]
print(len(dados))

count = 0
lista_dados1 = []
lista_dados2 = []
for i in dados:
    if(8.24 < i and i <= 8.28):
        lista_dados1.append(i)
        count += 1
    else:
        lista_dados2.append(i)
print(count)
print("Fazem parte", lista_dados1)
print("Não fazem parte", lista_dados2)         

