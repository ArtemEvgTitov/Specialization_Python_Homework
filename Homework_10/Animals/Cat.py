from Homework_10.Animals.Animal import Animal


class Cat(Animal):

    def __init__(self, name: str, age: int, purr: int):
        super().__init__(name, age, voise='Маукает', eat='Корм, птица, рыба')
        self.purr = purr

    def to_str(self):
        return super().to_str() + f'\nPurr level: Мурчатель-{self.speed}'

    def add_trophy(self, trophy):
        self.trophy = trophy
