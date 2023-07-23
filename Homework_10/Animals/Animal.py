class Animal:

    def __init__(self, name, age, voise, eat):
        self.name = name
        self.age = age
        self.voise = voise
        self.eat = eat

    def to_str(self):
        return f'\nName: {self.name}\nAge: {self.age}' \
               f'\nVoise: {self.voise}\nEat: {self.eat}'
