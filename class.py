class vehicle(object):
    def __init__(self,gas,price):
        self.price=price
        self.gas=gas
    def fullgas(self):
        self.gas=100
    def emptygas(self):
        self.gas=0
    def gasleft(self):
        return self.gas
class car(vehicle):
    def __init__(self,gas,price,color):
        super().__init__(gas,price)
        self.color=color
    def beep(self):
        print('beep beep')
class truck(car):
    def __init__(self,gas,price,color,tire):
        super().__init__(gas,price,color)
        self.tire=tire
    def beep(self):
        print('hank hank')
 

p1=vehicle(100,10000)
print(p1.price)
print(p1.gasleft())
p2=truck(400,50000,'yellow',8)
print(p2.color)