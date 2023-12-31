import json
import os
import csv
import pickle

# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.


def create_dict(path):
    """
    :param path: путь до директории
    :return: возвращает словарь, содержащий путь, вложенные директории и файлы, а также их размер
    """
    os.chdir(path)
    my_dict = {}
    id_path = 0
    total_size = 0
    for dir_path, dir_name, file_name in os.walk(os.getcwd()):
        for f in file_name:
            fp = os.path.join(dir_path, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
            my_dict[id_path] = {'Path': dir_path,
                                'Dir_name': dir_name,
                                'File_name': file_name,
                                'Size': total_size}
        id_path += 1
    return my_dict


def file_json(my_dict):
    """
    :param my_dict: словарь
    :return: Создаёт файл json
    """
    with open('dir.json', 'w', encoding='utf-8') as new_file_json:
        json.dump(my_dict, new_file_json, ensure_ascii=False)


def file_csv(my_dict):
    """
    :param my_dict: словарь
    :return: Создаёт файл csv
    """
    with open('dir.csv', 'w', newline='', encoding='utf-8') as new_file_csv:
        csv_write = csv.DictWriter(new_file_csv, fieldnames=["ID", "Path",
                                                         "Dir_name", "File_name", "Size"],
                                   dialect='excel-tab',
                                   quotechar='|',
                                   quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        all_data = []
        for i in my_dict:
            temp = {'ID': i,
                    'Path': my_dict[i]['Path'],
                    'Dir_name': my_dict[i]['Dir_name'],
                    'File_name': my_dict[i]['File_name'],
                    'Size': my_dict[i]['Size']}
            all_data.append(temp)
        csv_write.writerows(all_data)


def file_pickle(my_dict):
    """
    :param my_dict: словарь
    :return: Создаёт файл pickle
    """
    with open('my_dict.pickle', 'wb') as new_file_pickle:
        pickle.dump(my_dict, new_file_pickle, protocol=pickle.DEFAULT_PROTOCOL)


if __name__ == '__main__':
    test_dict = create_dict('D:\Studies\Specialization. Python. Homework\Homework_8')
    file_json(test_dict)
    file_csv(test_dict)
    file_pickle(test_dict)