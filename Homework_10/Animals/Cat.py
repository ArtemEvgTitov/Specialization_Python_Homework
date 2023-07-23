from Homework_10.Animals.Animal import Animal


class Cat(Animal):

    __health = 9

    def __init__(self, name, age, purr: int):
        super().__init__(name, age, voise='Маукает', eat='Корм, птица, рыба')
        self.purr = purr

    def to_str(self):
        return super().to_str() + f'\nPurr level: Мурчатель-{self.purr}\nHealth: {self.__health}'

    def up_purr(self, purr):
        if purr > self.purr:
            self.purr = purr
