class Comparações:
    def __init__ (self, a):
        self.a = a


    def __gt__(self, other):
        if (self.a > other.a):
            return True
        else:
            return False
        

    def __it__(self, other):
        if (self.a < other.a):
            return "É menor"
        else:
            return "É maior" 

    def __eq__(self, other):
        if (self.a == other.a):
            return "É igual"
        else:
            return "É diferente"      

num1 = Comparações(300)
num2 = Comparações(300)

print(num1.__gt__(num2))
print(num1.__it__(num2))
print(num1.__eq__(num2))


