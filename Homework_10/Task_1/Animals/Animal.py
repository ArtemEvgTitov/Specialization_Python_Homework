class Animal:
    """
    Класс для Animal.
    Содержит конструктор класса и метод печати to_str
    """

    def __init__(self, name: str, age: int, voise, eat):
        self.name = name
        self.age = age
        self.voise = voise
        self.eat = eat

    def to_str(self):
        return f'\nName: {self.name}\nAge: {self.age}' \
               f'\nVoise: {self.voise}\nEat: {self.eat}'
