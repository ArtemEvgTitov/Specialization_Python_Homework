from Homework_10.Animals.Animal import Animal


class Dog(Animal):

    def __init__(self, name, age, breed):
        super().__init__(name, age, voise='Лает', eat='Мясо, птица, рыба')
        self.commands = ['Сидеть', 'Лежать', 'Дай лапу']
        self.breed = breed

    def to_str(self):
        return super().to_str() + f'\nCommands: {self.commands}\nBreed: {self.breed}'

    def add_command(self, command):
        if command not in self.commands:
            self.commands.append(command)
