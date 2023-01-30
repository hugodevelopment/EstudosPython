
# Criando uma função para verificar o a situação do aluno
def situação(value,x):
   if (value > 7):
      print("Aprovado com ", value, x)
   else:
      print("Reprovado com ",value, x)   

alunos = ["Hugo", "Lucas", "Marcio", "Adonai"]
Notas =  [9,8,7,9]
Notas2 = [4,6,5,6]

media = 0
for i in range(len(alunos)):
   # print(alunos)
   # A variável soma pega o primeiro valor de notas e notas2 e faz a soma, por exemplo, 9+4, 6+8
   soma = Notas[i] + Notas2[i]
   # print(soma)
   media = soma/2
   situação(media, alunos[i]) 


for i in range(len(alunos)):
    soma = Notas[i] + Notas2[i]
    print(soma)
