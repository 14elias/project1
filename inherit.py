class dog(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greeting(self):
        print(f'hello{self.name}')
    def speak(self):
        print('bark')
class cat(dog):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color
    def speak(self):
        print('meow')
p1=dog('bitch',5)
print(p1.name)
p2=cat(' dimu',4,'black')
p2.greeting()
p2.speak()
p1.speak()