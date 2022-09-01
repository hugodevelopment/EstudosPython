# Criando minhas próprias funções

def myfirst():
    print("minha 1º função")
 

''' 
myfirst() # chamar a função antes de declarar resultará em erro
     def myfirst():
       print("minha 1º função")
'''

"-------------------------------------------------------------------------------------------------------------"
      
def foo(): # usamos foo para criar variaves ou funções de exemplo
   print(1)
   print(2)

foo() #irá printar 1 e 2
foo() #irá printar 1 e 2

"-------------------------------------------------------------------------------------------------------------"

#Criando argumentos para a função
def argumentos(texto): # a função recebe o argumento texto
    print(texto + " ok")
    
argumentos("tudo bem") #tudo bem virá texto e é printado na função argumentos

"-------------------------------------------------------------------------------------------------------------"

def dobro(x):    #função que imprime o dobro de x
   print(2 * x) # agora que x é 3, temos 2 * x que é 2 * 3 = 6 

dobro(3) # x será 3 agora na função
dobro(4) # x será 4 agora na função
dobro(5) # x será 5 agora na função

"-------------------------------------------------------------------------------------------------------------"

#Criando os argumentos x, y para print a soma deles (x+y)
def soma(x, y): 
    print(x + y)
    
soma(1, 3)
soma(1, 7)

"-------------------------------------------------------------------------------------------------------------"

#Criando a função par para avaliar se x é par ou impar
def par(x):
    if x%2 == 0:
        print("É par ",  x)
    else:
        print("É impar ", x)       
par(3)        

"-------------------------------------------------------------------------------------------------------------"

def msg(num, ch):
  print(ch+str(num))

msg(18, 'A')