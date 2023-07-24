from Homework_10.Task_1.Animals.Animal import Animal


class Cat(Animal):

    __health = 9
    __voise = 'Маукает'
    __eat = 'Корм, птица, рыба'

    def __init__(self, name, age, purr: int):
        super().__init__(name, age, self.__voise, self.__eat)
        self.purr = purr

    def to_str(self):
        return super().to_str() + f'\nPurr level: Мурчатель-{self.purr}\nHealth: {self.__health}'

    def up_purr(self, purr):
        if purr > self.purr:
            self.purr = purr
