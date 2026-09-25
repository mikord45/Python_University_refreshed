class Turtle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.__x = 0

    def say_name(self):
        print(f"Jestem żółwiem o imieniu {self.name} i mam prędkość {self.speed}.")

    def move(self, distance):
        self.__x += distance

    def get_position(self):
        return self.__x

john_turtle = Turtle("John", 5)
john_turtle.say_name()
john_turtle.move(10)
print(f"Aktualna pozycja: {john_turtle.get_position()}")

