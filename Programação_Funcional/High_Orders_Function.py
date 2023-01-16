
# Functional programming is a style of programming that (as the name suggests) is based around functions.
# A key part of functional programming is 
# higher-order functions. Higher-order functions take other functions as arguments, 
# or return them as results.

# Exemplo 1 

# Aqui temos uma função com dois argumetos, sendo um deles uma função
def test(func, arg):
   #neste caso a função mult é chamada 2x 
  return func(func(arg))

# Multiplica o parametro 2x
def mult(x):
  return x * x

print(test(mult, 3))


"--------------------------------------------------------------------------------------------------------------"
#  Higher Order Function =  a function that either:
#                           1. accepts a function as an argument
#                               or
#                           2. returns a function
#                           (In python, functions are also treated as objects)

# ----- 1. accepts a function as an argument -----
def shout(text):
  return text.upper()

def quiet(text):
  return text.lower()

def Hello(func):
  text = func("Oi, eu sou o goku")
  print(text)

Hello(shout)
Hello(quiet)  


# Python program to illustrate functions
# Functions can return another function

# 2. returns a function	
def create_mult(x):
  def number(y):
    return x *y
  return number

numero = create_mult(10)

print("multiplicando",numero(5))



