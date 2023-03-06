# You are making a drawing application, which has a Shape base class.
# The given code defines a Rectangle class, creates a Rectangle object and calls its area() and perimeter() methods.

# Do the following to complete the program:
# 1. Inherit the Rectangle class from Shape.
# 2. Define the perimeter() method in the Rectangle class, printing the perimeter of the rectangle.

# superclasse que defini algumas operações
class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print(self.width * self.height)

    def metade(self):
        print((self.width + self.height)/2)


# Criando o classe retangulo que herda os métodos da superclasse shape
class retangulo(Shape):
    def perimeter(self):
        print(2*(self.width + self.height))


w = 10
h = 20
# Aqui instanciamos a classe retangulo que herda os parametros(w,h) e os metodos da classe Shape
r = retangulo(w,h)
# Chamando o metodo area da superclasse Shape
r.area()
# Chamando o metodo metade da superclasse Shape
r.metade()
r.perimeter()
