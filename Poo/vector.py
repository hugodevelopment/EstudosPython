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

