import csv
import json
import pickle


class CreateFile:

    def __init__(self, my_dict):
        self.create_json(my_dict)
        self.create_csv(my_dict)
        self.create_pickle(my_dict)

    def create_json(self, my_dict):
        with open('dir.json', 'w', encoding='utf-8') as new_file_json:
            json.dump(my_dict, new_file_json, ensure_ascii=False)

    def create_csv(self, my_dict):
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

    def create_pickle(self, my_dict):
        with open('my_dict.pickle', 'wb') as new_file_pickle:
            pickle.dump(my_dict, new_file_pickle, protocol=pickle.DEFAULT_PROTOCOL)
