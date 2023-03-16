# class Pizza:
#     def __init__(self, toppings):
#         self.toppings = toppings

#     @property
#     def pineapple_allowed(self):
#         return False

# pizza = Pizza(["cheese", "tomato"])
# print(pizza.pineapple_allowed)
# pizza.pineapple_allowed = True


class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1
    
    #your code goes here
    @property
    def isAlive(self):
        if self._lives > 0:
            return True
        else:
             return False    
    

p = Player("Cyberpunk77", 7)
i = 1
while True:
    p.hit()
    print("Hit # " + str(i))
    i += 1
    if not p.isAlive:
        print("Game Over")
        break