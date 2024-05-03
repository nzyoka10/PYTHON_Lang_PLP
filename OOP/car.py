class Car:
    def __init__(self, make, model, year, color, name):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        # self.__name = name  # private attribute with double underscore to indicate it's not meant for direct access from outside the class
    
    def drive(self):
        print("Drive Method!")
    
    def stop(self):
        print("Stop Method!")
        
# Create an instance of the Car class
car_1 = Car("Chevy", "Corvette", 2021, "Blue")

# Output car attributes
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)