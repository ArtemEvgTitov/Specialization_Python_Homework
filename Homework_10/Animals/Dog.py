from Homework_10.Animals.Animal import Animal


class Dog(Animal):

    def __init__(self, name, age):
        super().__init__(name, age, voise='Лает', eat='Мясо, птица, рыба')
        self._commands = ['Сидеть', 'Лежать', 'Дай лапу']

    def to_str(self):
        return super().to_str() + f'\nCommands: {self._commands}'

    def add_command(self, command):
        if command not in self._commands:
            self._commands.append(command)
