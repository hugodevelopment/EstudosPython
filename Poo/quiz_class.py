

# You need to do the following to complete the program:
# 1. Inherit the Alien and Monster classes from the Enemy class.
# 2. Complete the while loop that continuously takes 
# the weapon of choice from user input and call the corresponding object's hit() method.


class Enemy:
  name = ""
  lives = 0
  def __init__(self, name, lives):
    self.name = name
    self.lives = lives

  def hit(self):
    self.lives -= 1
    if self.lives <= 0:
       print(self.name + ' killed')
    else:
        print(self.name + ' has '+ str(self.lives) + ' lives')

class Monster(Enemy):
  def __init__(self):
    super().__init__('Monster', 3)

class Alien(Enemy):
  def __init__(self):
    super().__init__('Alien', 5)


m = Monster()
a = Alien()

while True:
    x = input()
    if x == "laser":
        a.hit()
    elif x == "gun":    
        m.hit()
    elif x == 'exit':
        break