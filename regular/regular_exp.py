import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ
phone_pattern = r"(\+7|8)?\s*[(]?(\d{3})[)]?\s?[-]?(\d{3})[-]*(\d{2})[-]*(\d{2})\s?\(?([доб.]{4})?\s?(\d{4})?"
sub_pattern = r"+7(\2)\3-\4-\5 \6\7"

for line in contacts_list:
    changed_line = re.sub(phone_pattern, sub_pattern, line[-2])
    line[-2] = changed_line
pprint(contacts_list)

phones = []
    # for element in line:
    #     if re.search(phone_pattern, element):
    #         print('yes')
    #         re.sub(phone_pattern, 'asshole', element)
    #         print(element)
    # #     phones.append(re.search(phone_pattern, line))

# for line in phones:
#     for item in line:
#         if item[-2] == '':
#             line.pop(0)
#             line.append(item[:-2])
# pprint(phones)
# pprint(contacts_list)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#     # Вместо contacts_list подставьте свой список
#     datawriter.writerows(text)
