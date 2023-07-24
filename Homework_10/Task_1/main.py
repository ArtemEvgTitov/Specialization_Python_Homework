from Animal_factory import AnimalFactory


if __name__ == '__main__':

    all_animals = []

    name = 'Джек'
    age = 7
    breed = 'Лайка'

    dog = AnimalFactory.create_animal('Dog', name, age, breed)
    all_animals.append(dog)

    name = 'Кондор'
    age = 5
    speed = 60

    horse = AnimalFactory.create_animal('Horse', name, age, speed)
    all_animals.append(horse)

    name = 'Мурка'
    age = 5
    purr = 3000

    horse = AnimalFactory.create_animal('Cat', name, age, purr)
    all_animals.append(horse)

    for animal in all_animals:
        print(animal.to_str())
