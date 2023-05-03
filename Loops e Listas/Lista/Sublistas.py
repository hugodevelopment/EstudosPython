# Em python podemos obter sublistas utilizando o slice

lista1 = [1,2,3,4,5,6,7,8,9,10]
# Sublista de 0 a 5, mas é importante ter cuidado que ele não está olhando o número, mas sim a POSIÇÃO!
sublista1 = lista1[0:5]
# A posição do ultimo item não é inclusa, ou seja, de 0 a 5, ele vai até 4
print(sublista1)

# Verificando novamente a posição, iremos começar do 1 até a posição 4
sublista2 = lista1[1:5]
print(sublista2)

# Se quisermos fazendo passo a passo, fazemos para pegar os itens em 2 em 2: 
sublista3 = lista1[1::2]
print(sublista3)

# ---------------------------------------------- Matrizes -----------------------------------------------------------------**

# Matrizes em programação são listas dentro de listas:

Matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

# Podemos obter a primeira linha da matriz (ou seja, a sublista correspondente à primeira lista da matriz) da seguinte forma:
linha1 = Matriz[0]
print(linha1)

# Podemos obter a submatriz correspondente às 
# duas primeiras linhas e duas primeiras colunas da matriz original da seguinte forma:

# podemos pegar todas as linhas utilizando list comprehession, indo de 0:3 para conter o ultimo elemento
todas_linhas = [linha[0:3] for linha in Matriz]
print(linha)








