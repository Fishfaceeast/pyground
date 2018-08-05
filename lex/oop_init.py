class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hi, I am ', self.name)


person = Person("Jimmy")
person.say_hi()