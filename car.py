class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
            print(f"{self.brand} {self.model} {self.year} is starting")

    def stop(self):
            print(f"{self.brand} {self.model} {self.year} is stopping")

    def display_info(self):
            print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")                

P = Car("Toyota", "Land Cruiser", 2025)
P.display_info()
P.start()
P.stop()