#Criando o arquivo para ler a função alunos

# Importante o arquivo com a função que retornar a lista dos alunos
import alunos
import media
import observacao
import lista_total
import pesquisa
import pesquisa_total
# Criando uma variável para salvar a quantidade de alunos
Total_Alunos = int(input("Quantos alunos são :"))
# Criando a lista de alunos vazia
lista_alunos = []
media_alunos = []
lista_observacao = []
lista_geral = []
for i in range(Total_Alunos):
    # preenchendo a lista de alunos com as informações da função alunos_info
    lista_alunos.append(alunos.alunos_info())
    media_alunos.append([lista_alunos[i][0],media.calc_media(lista_alunos[i][1],lista_alunos[i][2],lista_alunos[i][3])])
    lista_observacao.append([lista_alunos[i][0],observacao.obs()])
    lista_geral.append(lista_total.lista_total(lista_alunos[i][0],lista_alunos[i][1],lista_alunos[i][2],lista_alunos[i][3],media_alunos[i][1],lista_observacao[i][1]))
print(lista_alunos)
print(media_alunos)
print(lista_observacao)
print(lista_geral)    

pesquisa.pesquisa_nome(lista_alunos[i][0], lista_geral)
pesquisa_total.pesquisa_final(lista_geral)
