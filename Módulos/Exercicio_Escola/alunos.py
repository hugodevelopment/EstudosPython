# Criando o módulo para salvar nomes e as notas

#Criando a função alunos que recebe o nome  e as 3 notas
def alunos_info():
   nome  = input('Digite seu nome: ')
   nota1 = float(input("Digite a 1º nota: "))
   nota2 = float(input("Digite a 2º nota: "))
   nota3 = float(input("Digite a 3º nota: "))
   #Neste caso função irá retornar uma lista com o nome e as três notas dos alunos
   return([nome,nota1,nota2,nota3])

   




