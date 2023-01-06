
def dobro(x):
    # Criando uma lista vazia para receber o resultado
    resultado = []
    # Loop para calcular a lista de numeros
    for i in x:
        # Criando o calculo para elevar os números ao quadrado
        resultado.append(x**2)
    return resultado    

lista = [1, 4, 9, 20]
print(dobro(lista))

"----------------------------------------------------------------------------------------------------------------------------------"

fruits = ["apple", "banana", "cherry", "kiwi", "mango", "uvu"]

nova_lista = []
def novalista(x):
  if "a" in x:
      nova_lista.append(x)
  return nova_lista
    	
for i in fruits:
	novalista(i)
print("1",nova_lista)    

   
    
    
	

    	




