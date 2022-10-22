
# nums = []
# i=0
# # O laço será executado enquanto o tamanho da
# # lista nums for menor que 4
# print("Para sair escolha -1")
# while True:
#     # Pede ao usuário uma entrada e a armazena em uma variável como número inteiro.
#     user_input = int(input("Insira um número inteiro: "))
#     if user_input == -1:
#         break
#     else:
#         nums.append(user_input)
#         i += 1
# print("o tamanho da lista é", i) 
# print("com len", len(nums))
# print(nums) 


nums = []
def lista(valores):
    nums.append(valores) 
    print("A lista tem tamanho:", len(nums))
    return (len(nums))


while True:
     # Pede ao usuário uma entrada e a armazena em uma variável como número inteiro.
    valores = int(input("Insira um número inteiro: "))
    if valores == -1:
        print(nums)
        break
    else:
        lista(valores)


