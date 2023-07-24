from Homework_10.Task_1.Animals.Animal import Animal


class Horse(Animal):

    __voise = 'Ржёт'
    __eat = 'Сено, солома, овёс, трава'

    def __init__(self, name, age, speed: int):
        super().__init__(name, age, self.__voise, self.__eat)
        self.trophy = None
        self.speed = speed

    def to_str(self):
        return super().to_str() + f'\nSpeed: {self.speed}\nTrophy: {self.trophy}'

    def add_trophy(self, trophy: str):
        self.trophy = trophy
