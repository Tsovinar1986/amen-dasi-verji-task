from math import *


class Coronavirus:
    def __init__(self,temperature):
        self.temperature = temperature
        
    def show(self):
        self.temperature = floor(self.temperature * pi)
        if 120 <= self.temperature <= 128:
            return 'You have coronavirus'
        else:
            return 'Everuthing is ok'       
        
temperature = float(input('Enter temperature in Celsius please --> '))
x = Coronavirus(temperature)
print(x.show())
