class Animals:
    def speak(self):
        print('Animal is speaking')
class Dog(Animals):
    def bark(self):
        print('Dog is barking')
class Cat(Animals):
    def meows(self):
        print('Cat is meowing')
    def drinks_milk(self):
        print('Cat is drinking milk')
class Cow(Animals):
    def moos(self):
        print('Cow is mooing')


d=Dog()
d.bark()
c=Cat()
c.meows()
c.drinks_milk()
e=Cow()
e.moos()
d.speak()

class Cars:
    def drive(self):
        print('Cars drive')
class Toyota(Cars):
    def Japan(self):
        print('Toyota is made in japan')
class Landrover(Cars):
    def Britain(self):
        print('Landrover is made in britain')
class Tesla(Cars):
    def USA(self):
        print('Tesla is made and based in USA')
class Mahindra(Cars):
    def Kenya(self):
        print('Mahindra is made and assembled in Kenya')
class BMW():
    def Germany(self):
        print('BMW is made in Germany')

a=Toyota()
a.Japan()
b=Landrover()
b.Britain()
c=Tesla()
c.USA()
d=Mahindra()
d.Kenya()
e=BMW()
e.Germany()


