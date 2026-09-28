class Simplest:
    pass

print(type(Simplest))
print(Simplest.__bases__)

Simplest.a = 5
print(Simplest.a)

s1 = Simplest()
print(s1)
print(type(s1))
s1.b = 10
print(s1.b)
print(s1.a)
print(s1.a is Simplest.a)
s1.a = 15
print(s1.a)
print(Simplest.a)
# print(s1.c)
Simplest.c = 30
print(s1.c)
print("----")

def explode(self):
    print("bum")

Simplest.explode = explode
Simplest.explode(s1)
s1.explode()

class Samochod:
    def __init__(self, name):
        self.name = name
        self.counter = 0
    def go(self, distance):
        self.counter += distance
        print("jazda")

ferrari = Samochod('ferrari')
ferrari.go(50)
ferrari.go(80)
print(ferrari.counter)

class Truck(Samochod):
    def go(self):
        super().go(50)
        print('jazda ciezarowka')

tir = Truck('Lambo')
tir.go()
tir.go()
print(tir.counter)

Samochod.go(tir, 50)
print(tir.counter)
Samochod.go(ferrari, 100)
print(ferrari.counter)
super(Truck, tir).go(150)
print(tir.counter)

def new_go(self, distance):
    print('nowe go')
    self.counter += 1000
Samochod.go = new_go
ferrari.go(500)
print(ferrari.counter)
