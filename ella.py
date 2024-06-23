class cat(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        print(f'hello {self.name} how are you')
    def talk(self):
        print('bark')
class dog(cat):
    def talk(self):
        print('meow')
p1=cat('dmet',5)
p1.speak()
p1.talk()
p2=dog('bitch',6)
p2.speak()
p2.talk()