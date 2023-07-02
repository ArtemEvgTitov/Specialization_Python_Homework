# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def keyword_parameters(**kwargs):
    data = {}
    for key, value in kwargs.items():
        if not hashable(key):
            key = str(key)
        data.update({f'{value}': key})
    return data


def hashable(key):
    try:
        hash(key)
        return True
    except TypeError:
        return False


print(keyword_parameters(Петя=4, Костя=5, Юля=3, Андрей=list('6')))
