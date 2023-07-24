from Animal_factory import AnimalFactory


if __name__ == '__main__':

    all_animals = []

    name = 'Джек'
    age = 7
    breed = 'Лайка'

    dog = AnimalFactory.create_animal('Dog', name, age, breed)
    dog.add_command('Рядом')
    all_animals.append(dog)

    name = 'Кондор'
    age = 5
    speed = 60

    horse = AnimalFactory.create_animal('Horse', name, age, speed)
    horse.add_trophy('Любимец публики')
    all_animals.append(horse)

    name = 'Мурка'
    age = 7
    purr = 666

    cat = AnimalFactory.create_animal('Cat', name, age, purr)
    cat.up_purr(3000)
    all_animals.append(cat)

    for animal in all_animals:
        print(animal.to_str())
