# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

def remove_duplicates(my_list):
    result = []
    for item in my_list:
        if item not in result:
            result.append(item)
    return result


my_list = [1, 1, 2, 2, 3, 4, 5, 5, 1, 3, 6, 7, 8, 8, 9]
my_list = remove_duplicates(my_list)
print(my_list)
