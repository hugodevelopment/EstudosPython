
def procurar_alunos(alunos,pesquisa):
    for i in alunos:
        chave = alunos[i]
        if chave["nome"] == pesquisa:
             print("Aluno encontrado \n", chave)