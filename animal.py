class animal:
    def bark(self):
        print("Woof woof!")

class dog(animal):
    def eat(self):
        print("Bark bark!")

dog1 = dog()
dog1.bark()
dog1.eat()      