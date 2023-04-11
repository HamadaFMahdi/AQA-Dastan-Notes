# Polymorphism

class Animal:
    def __init__(self, name):
        self.name = name
    def make_noise(self):
        print("Making noise...")
    def _complex_health_check(self):
        print("some long complicated code")
        print("some long complicated code")
        print("some long complicated code")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.whiskers = True


    def make_noise(self):
        print("Meow!")

    def complex_health_check(self):
        super()._complex_health_check()
        print("Cat specific check")

class Dog(Animal):
    def make_noise(self):
        print("Woof!")

animal1 = Animal('Animal1')
cat1 = Cat('Cat1')
dog1 = Dog('Dog1')

animal1.make_noise()
cat1.make_noise()
dog1.make_noise()

animals = [animal1, cat1, dog1]
for animal in animals:
    animal.make_noise()
