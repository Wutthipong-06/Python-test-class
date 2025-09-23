class Car:
    # Class attribute
    wheels = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engin(self):
        return f'The engin of the {self.year} {self.make} {self.model} in now running.'
    
    def stop_engin(self):
        return f'The engin of the {self.year} {self.make} {self.model} is now off.'
    
my_car = Car('Toyota', 'Camry', 2020)
print(my_car.make)
print(my_car.model)
print(my_car.year)

print(my_car.start_engin())
print(my_car.stop_engin())
