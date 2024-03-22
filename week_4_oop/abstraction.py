# Abstraction in Python
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
   