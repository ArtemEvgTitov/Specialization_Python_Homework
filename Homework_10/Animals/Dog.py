from Homework_10.Animals.Animal import Animal


class Dog(Animal):

    __voise = 'Лает'
    __eat = 'Мясо, птица, рыба'

    def __init__(self, name, age, breed: str):
        super().__init__(name, age, self.__voise, self.__eat)
        self.commands = ['Сидеть', 'Лежать', 'Дай лапу']
        self.breed = breed

    def to_str(self):
        return super().to_str() + f'\nCommands: {self.commands}\nBreed: {self.breed}'

    def add_command(self, command):
        if command not in self.commands:
            self.commands.append(command)
