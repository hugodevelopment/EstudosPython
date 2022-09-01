import media 
import situacao
import observacao
def cadAlunos():
    Nome = input("Insira o nome do Aluno: ")
    Nota1 = int(input("Digite a 1º Nota: "))
    while(Nota1> 10):
        print("Nota de 0 a 10, digite novamente")
        Nota1 = int(input("Digite a 1º Nota: "))
    Nota2 = int(input("Digite a 2º Nota: "))
    Nota3 = int(input("Digite a 3º Nota: "))
    med = media.media(Nota1,Nota2,Nota3)
    situacao_aluno = situacao.situacao_func(med,Nome)
    obs = observacao.obs_aluno()
    return ({
         "nome":Nome,
         "nota1": Nota1,
         "nota2": Nota2,
         "nota3": Nota3,
         "media": med,
         "Situação":situacao_aluno,
         "Observaçao":obs
        })
        
   
      
            