# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def split_path(path):
    parts = path.split('/')
    file_name = parts[-1]
    file_path = '/'.join(parts[:-1])
    file_name_parts = file_name.split('.')
    if len(file_name_parts) > 1:
        file_ext = '.' + file_name_parts[-1]
        file_name = '.'.join(file_name_parts[:-1])
    else:
        file_ext = ''
    return file_path, file_name, file_ext


result = (split_path('D:/Studies/Bot/README.md'))
print(result)

