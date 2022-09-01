import cadastroAlunos
import pesquisa_aluno

Total_de_alunos = int(input("Insira a Quantidade de Alunos: "))

while(Total_de_alunos <= 0):
    print("Tem que ser maior que 1, tente novamente")
    Total_de_alunos = int(input("Insira a Quantidade de Alunos:"))

print()
print("---------- Bem vindo ao programa escola-------")

alunos={}

for dados_alunos in range(Total_de_alunos):
    alunos.update({dados_alunos:cadastroAlunos.cadAlunos()})

#Estou tentando criar um menu

print()

print("--------- Bem Vindo ao Menu----------")


menu = input( '''
1-Busca por aluno
2-Todos os alunos
''')

escolha = ""
 
while escolha != "sair":
        if menu == "1":
            nome = input("Nome: ")
            print(pesquisa_aluno.procurar_alunos(alunos,nome))
            # escolha = input("Digite sair para finalizar: ")

        elif menu == "2":
            print(alunos)
            # escolha = input("Digite sair para finalizar: ")
        escolha = input("Digite sair para finalizar: ")

        
