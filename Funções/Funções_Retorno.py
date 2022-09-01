

#Criando a função soma com x e y como argumentos
def sum(x, y):
  return x+y
# Retornar é útil quando você não precisa imprimir o resultado da função, mas precisa usá-lo em seu código. 

x = int(input("Digite um numero: "))
y = int(input("Digite outro numero: "))
# Criamos uma variável para printar o resultado
res = sum(x, y)
print(res) 

#Podemos colocar o resultado dentro do print também
print("A soma de x e y é :", sum(x,y))