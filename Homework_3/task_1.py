# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

def remove_duplicates(my_list):
    result = []
    for item in my_list:
        if item not in result:
            result.append(item)
    return result

def remove_duplicates2(my_list):
    result = list(set(my_list))
    return result

my_list = [1, 1, 2, 2, 3, 4, 5, 5, 1, 3, 6, 7, 8, 8, 9]
my_list1 = remove_duplicates(my_list)
my_list2 = remove_duplicates2(my_list)
print(my_list1)
print(my_list2)
