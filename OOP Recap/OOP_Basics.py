# Basics

class Cat:
    def __init__(self, name, colour):
        # constructor
        # instantiates an object
        # creates an instance/object of class
        # instance and object are synonymous
        self.name = name
        self.colour = colour
        self.energy = 100

    def eat(self, food):
        print(f"{self.name} is eating {food}")
        self.energy += 50

noir = Cat('Noir', 'Black')
noir.eat('Fish')
tyrone = Cat('Tyrone', 'White')
# tyrone.eat('Chicken')
print(noir.energy)
print(tyrone.energy)
# eat(noir, 'Fish')
