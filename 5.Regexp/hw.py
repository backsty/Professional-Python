from pprint import pprint
import csv
import re
import operator
import os
import itertools
from collections import defaultdict

directory = r'C:\Users\Shala\OneDrive\Рабочий стол\Professional Python\regular expressions\Regular expressions hw'


# Чтение данных из csv файла в отдельный список словарей
def read_csv_file(file_name):
    """
    Reads data from a CSV file and returns a list of dictionaries.

    :param file_name: name CSV file
    :return: A list of dictionaries representing data from CSV.
    """
    contact_dict = []
    with open(file_name, encoding="utf-8") as file:
        rows = csv.reader(file, delimiter=",")
        contact_list = list(rows)
    # pprint(contact_list)

        # Воспользуемся словарём для удобства
        keys = contact_list[0]
        values = contact_list[1:]
        # contact_dict = [dict(zip(keys, val)) for val in values]
        for number, val in enumerate(values):
            contact_dict.append({})
            for key, value in zip(keys, val):
                contact_dict[number].update({key: value})
        # pprint(contact_dict)
        return contact_dict


# Запись исправленных данных в новый csv файл
def write_dicts_to_new_file(file_name, dicts):
    """
    Writes data from dictionaries to a new CSV file.

    :param file_name: The name of the new CSV file.
    :param dicts: A list of dictionaries to write to a file.
    :return: None
    """
    keys = list(dicts[0].keys())
    # pprint(keys)
    with open(file_name, "w", encoding="utf-8", newline='') as file:
        datawriter = csv.DictWriter(file, fieldnames=keys)
        datawriter.writeheader()
        datawriter.writerows(dicts)


def fix_phone_num(in_the_file, out_of_the_file):
    """
    Corrects the format of the phone numbers in the specified file.

    :param in_the_file: The source file with the data.
    :param out_of_the_file: A new file for recording corrected data.
    :return: None
    """
    with open(in_the_file, encoding="utf-8") as file:
        text = file.read()

    patter_phone_num = r'(\+7|8)?\s*\(?(\d{3})\)?[\s*-]?(\d{3})[\s*-]?(\d{2})[\s*-]?(\d{2})(\s*)\(?(доб\.?)?\s*(\d*)?\)?'
    fixed_phone_num = re.sub(patter_phone_num, r'+7 (\2) \3-\4-\5\6\7\8', text)
    # pprint(fix_phone_num)
    with open(out_of_the_file, "w", encoding="utf-8") as file:
        file.write(fixed_phone_num)


def fix_personal_data(in_the_file):
    """
    Corrects the format of the personal data in the specified file.

    :param in_the_file: The name of the source data file.
    :return: A list of dictionaries with the corrected format of personal data.
    """
    contact_dict = read_csv_file(in_the_file)
    for val in contact_dict:
        spliting = val['lastname'].split(' ')
        if len(spliting) > 1:
            val['lastname'] = spliting[0]
            val['firstname'] = spliting[1]
            if len(spliting) > 2:
                val['surname'] = spliting[2]

        spliting = val['firstname'].split(' ')
        if len(spliting) > 1:
            val['firstname'] = spliting[0]
            val['surname'] = spliting[1]

    # pprint(contact_dict)
    return contact_dict


def merges_personal_datas(contacts):
    """
    Combines a list of dictionaries of personal data, comparing by last name and first name.

    :param contacts: A list of personal data dictionaries.
    :return: A list of combined dictionaries of personal data.
    """
    merged_data = defaultdict(dict)

    for contact in contacts:
        key = (contact.get('lastname', ''), contact.get('firstname', ''))
        if not merged_data[key]:
            merged_data[key] = contact
        else:
            for k, v in contact.items():
                if not merged_data[key][k] and v:
                    merged_data[key][k] = v

    return list(merged_data.values())


if __name__ == '__main__':
    contacts = read_csv_file("phonebook_raw.csv")

    fix_phone_num("phonebook_raw.csv", os.path.join(directory, "fix_tel_num.csv"))
    fixed_contacts = read_csv_file(os.path.join(directory, "fix_tel_num.csv"))

    fixed_personal_data = fix_personal_data(os.path.join(directory, "fix_tel_num.csv"))

    # Объединение дублирующихся записей
    merged_personal_data = merges_personal_datas(fixed_personal_data)

    # Запись объединенных данных в новый файл
    write_dicts_to_new_file(os.path.join(directory, "phonebook.csv"), merged_personal_data)

    # Удаление промежуточного файла с исправленными телефонами
    os.remove(os.path.join(directory, "fix_tel_num.csv"))
