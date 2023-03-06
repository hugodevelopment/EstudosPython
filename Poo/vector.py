class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

vetor1 = vector(2,3)
vetor2 = vector(4,4)

print("normal", vetor1 + vetor2)
print("com magic methods", vetor1.__add__(vetor2))

