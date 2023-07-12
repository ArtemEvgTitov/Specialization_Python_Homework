# Напишите функцию группового переименования файлов. Она должна:
#   принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
#   принимать параметр количество цифр в порядковом номере.
#   принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
#   принимать параметр расширение конечного файла.
#   принимать диапазон сохраняемого оригинального имени.
#       Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
#       К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os


def rename_files(desired_name, num_digits, source_extension, destination_extension, name_range=None):
    """
    desired_name: желаемое конечное имя файла.\n
    num_digits: количество цифр в порядковом номере.\n
    source_extension: расширение исходного файла.\n
    destination_extension: расширение конечного файла.\n
    name_range: диапазон сохраняемого оригинального имени.
    """
    file_counter = 1

    for filename in os.listdir('.'):
        if filename.endswith(source_extension):
            name_part = filename[name_range[0] - 1:name_range[1]]
            new_name = f"{name_part}_{desired_name}_{str(file_counter).zfill(num_digits)}.{destination_extension}"
            os.rename(filename, new_name)
            file_counter += 1

if __name__ == '__main__':
    rename_files('testing', 3, '.docx', 'txt', [0, 0])
