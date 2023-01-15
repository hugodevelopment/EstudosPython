
# Functional programming is a style of programming that (as the name suggests) is based around functions.
# A key part of functional programming is 
# higher-order functions. Higher-order functions take other functions as arguments, 
# or return them as results.


def test(func, arg):
  return func(func(arg))

def mult(x):
  return x * x

print(test(mult, 3))