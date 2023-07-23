from Homework_10.Animals.Animal import Animal


class Horse(Animal):

    def __init__(self, name, age, speed: int):
        super().__init__(name, age, voise='Ржёт', eat='Сено, солома, овёс, трава')
        self.trophy = None
        self.speed = speed

    def to_str(self):
        return super().to_str() + f'\nSpeed: {self.speed}\nTrophy: {self.trophy}'

    def add_trophy(self, trophy: str):
        self.trophy = trophy
