class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def eat(self):
        print("Dog is eating...")
        super().eat()  # 

dog = Dog()
dog.eat()  

                