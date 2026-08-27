class Dog:
    def bark(self):
        print("Woof woof!")

class Goat:
    def bark(self):
        print("Baa baa!")

class Horse:
    def bark(self):
        print("Neigh neigh!")


animals = [Dog(), Goat(), Horse()]
for animal in animals:
    animal.bark()                        