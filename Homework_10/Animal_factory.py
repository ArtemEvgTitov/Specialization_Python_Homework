from Animals.Dog import Dog
from Animals.Horse import Horse
from Animals.Cat import Cat


class AnimalFactory(Dog, Horse, Cat):

    def create_dog(self, name, age, breed):
        Dog.__init__(self, name, age, breed)

    def create_horse(self, name, age, speed):
        Horse.__init__(self, name, age, speed)

    def create_cat(self, name, age, purr):
        Cat.__init__(self, name, age, purr=3000)
