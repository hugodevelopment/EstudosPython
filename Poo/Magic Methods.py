# Magic methods are special methods which have double underscores at the beginning and end of their names.
# They are also known as dunders.
# So far, the only one we have encountered is __init__, but there are several others.

# De forma natural utilizando o operador (+):
print(1 + 3)
print("Hugo" + " Alves")

# Porém, podemos usar uma classe para isso

class Soma:
    def __init__(self,x):
        self.x = x
    # metodo add para realizar a soma 
    def __add__(self, y):
        return(self.x + y.x) 

# instanciando a classe Soma
num1 = Soma(3)
num2 = Soma(4)
num3 = Soma(5)

palavra1 = Soma("hugo")
palavra2 = Soma("lucas")

# Somando com o metodo convencional
result = palavra1 + palavra2
print("soma de palavras", result)

print("Soma convencional", num1 + num2)
# Somando com o magic methods
print("Soma com magic methods", num1.__add__(num2))
print("Soma de palavras com magic methods", palavra1.__add__(palavra2))

