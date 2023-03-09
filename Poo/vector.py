class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y
    
    def __eq__(self, other):
        if (self.x == other.x):
            return "Iguais"
        else:
            return "diferentes"

vetor1 = vector(3,3)
vetor2 = vector(2,4)

print("normal", vetor1 + vetor2)
print("com magic methods", vetor1.__add__(vetor2))
print(vetor1 == vetor2)


class Shape: 
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width*self.height

    #your code goes here
    def __add__(self, other):
        return Shape(self.width + other.width, self.height + other.height)

    def __gt__(self,other):
        if (self.area() > other.area()):
            return True
        else:
            return False         
    

w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)
result = s1 + s2

print(result.area())
print(s1 > s2)

   
