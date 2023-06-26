# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

def generate_subsets(items):
    subsets = [[]]

    for item in items:
        new_subsets = []

        for subset in subsets:
            new_subset = subset + [item]
            new_subsets.append(new_subset)

        subsets.extend(new_subsets)

    return subsets


def find_backpack_combinations(backpack_capacity, items):
    valid_combinations = []

    for subset in generate_subsets(items):
        total_weight = sum(item[1] for item in subset)

        if total_weight <= backpack_capacity:
            valid_combinations.append(subset)

    return valid_combinations


items = {
    "Тент": 2,
    "Спальный мешок": 1,
    "Компас": 0.1,
    "Фонарик": 0.2,
    "Палатка": 3,
    "Котелок": 0.5
}

backpack_capacity = 5
valid_combinations = find_backpack_combinations(backpack_capacity, list(items.items()))

for combination in valid_combinations:
    print("Вариант:", combination)
    total_weight = sum(item[1] for item in combination)
    print("Общий вес:", total_weight)
    print("--------------------")