from Animals.Dog import Dog
from Animals.Horse import Horse
from Animals.Cat import Cat


class AnimalFactory:

    @staticmethod
    def create_animal(animal_type, *args, **kwargs):
        if animal_type == "Dog":
            return Dog(*args, **kwargs)
        elif animal_type == "Horse":
            return Horse(*args, **kwargs)
        elif animal_type == "Cat":
            return Cat(*args, **kwargs)
        else:
            raise ValueError("Invalid animal type")
