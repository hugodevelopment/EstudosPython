class Maior:
    def __init__ (self, a):
        self.a = a


    def __gt__(self, other):
        if (self.a > other.a):
            return True
        else:
            return False

num1 = Maior(400)
num2 = Maior(300)

print(num1.__gt__(num2))


