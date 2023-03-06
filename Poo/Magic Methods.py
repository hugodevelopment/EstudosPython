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

    def __add__(self, y):
        return(self.x + y.x) 


num1 = Soma(3)
num2 = Soma(4)

palavra1 = Soma("hugo")
palavra2 = Soma("lucas")

result = palavra1 + palavra2
print("soma de palavras", result)

print("Soma convencional", num1 + num2)
print("Soma com magic methods", num1.__add__(num2))
print("Soma de palavras com magic methods", palavra1.__add__(palavra2))
