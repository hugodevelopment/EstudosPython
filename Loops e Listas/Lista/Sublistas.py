# Em python podemos obter sublistas utilizando o slice

lista1 = [1,2,3,4,5,6,7,8,9,10]
# Sublista de 0 a 5, mas é importante ter cuidado que ele não está olhando o número, mas sim a POSIÇÃO!
sublista1 = lista1[0:5]
print(sublista1)

# A posição do ultimo item não é inclusa, ou seja, de 0 a 5, ele vai até 4