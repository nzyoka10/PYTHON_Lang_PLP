# 
#* ********   Python Object Oriented Programming 
# Vehicle class
# 
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def start(self):
        raise NotImplementedError("Start is not implemented")
    
    def stop(self):
        raise NotImplementedError("Stop is not implemented")
    
class Car(Vehicle):
    def start(self):
        return f"I own a {self.year} {self.make} {self.model}, start() method"
    
    def stop(self):
        return f"The {self.year} {self.make} {self.model}, stop() method"
    
class Motorcycle(Vehicle):
    def start(self):
        return f"The {self.year} {self.make} {self.model} ravs the orgina and starts"
    
    def stop(self):
        return f"The {self.year} {self.make} {self.model} applies the brakes and stops"
    
# ----------------------------------------------------------------
print(" *********  Python OOP ********* \n")
#*   ------  Instances of classes Car and Motorcycle ------
my_car = Car("Mercedes Benz", "C 200", 2020)
my_motorcycle = Motorcycle("Honda", "CBR500R", 2020)

# * * * * * * * * * * * * * * * * *
# use of the START and STOP method 
print("Car class : ", my_car.start())
print("Car : ", my_car.stop())

print('\n')

print("Motorcycle class: ", my_motorcycle.start())
print("Motorcycle: ", my_motorcycle.stop())


# print('\t \n', type(my_car))


