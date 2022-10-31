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

name_pattern = r"([А-Я]\w+)(.?)([А-Я]\w+)(.?)([А-Я]\w+)?"
sub_name_pattern = r"\1 \3 \5 "

organization_pattern = r"[,]([А-Я]{3})[,]|[,]([А-Я]\w+)[,]\W"
sub_organization_pattern = r" \1\2 "

for line in contacts_list:
    changed_phone_line = re.sub(phone_pattern, sub_pattern, line[-2])
    line[-2] = changed_phone_line

    line_name = ' '.join(line[0:3])
    changed_name_line = re.sub(name_pattern, sub_name_pattern, line_name)
    changed_name_line = changed_name_line.split()

    for i in range(len(changed_name_line)):
        line[i] = changed_name_line[i]

    changed_organization_line = re.sub(organization_pattern, sub_organization_pattern, line[3])
    line[3] = changed_organization_line
pprint(contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#     # Вместо contacts_list подставьте свой список
#     datawriter.writerows(text)
