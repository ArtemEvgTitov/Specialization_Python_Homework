import os


class CreateDict:
    """
    Класс для CreateDict.
    Создаёт экземпляр класса со словарём, содержащим
    вложенные директории и файлы, а также их размер
    """

    def __init__(self, path):
        self.my_dict = self.__create_dict(path)

    def __create_dict(self, path):
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
