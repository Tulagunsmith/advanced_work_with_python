import re
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# TODO 1: выполните пункты 1-3 ДЗ
phone_pattern = r"(\+7|8)?\s*[(]?(\d{3})[)]?\s?[-]?(\d{3})[-]*(\d{2})[-]*(\d{2})\s?\(?([доб.]{4})?\s?(\d{4})?"
sub_pattern = r"+7(\2)\3-\4-\5 \6\7"

name_pattern = r"([А-Я]\w+)(.?)([А-Я]\w+)(.?)([А-Я]\w+)?"
sub_name_pattern = r"\1 \3 \5 "

organization_pattern = r"[,]([А-Я]{3})[,]|[,]([А-Я]\w+)[,]\W"
sub_organization_pattern = r" \1\2 "

position_pattern = r"[,]\b(\w+\s\b\w+\s.?\s?\b\w+\s\w+\s\w+.+?)[,]"
sub_position_pattern = r"\1"

email_pattern = r"\d?[,]?(\b[A-Za-z0-9]+@\w+.\w{,3})"
sub_email_pattern = r"\1"

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

    changed_position_line = re.sub(position_pattern, sub_position_pattern, line[4])
    line[4] = changed_position_line

    changed_email_line = re.sub(email_pattern, sub_email_pattern, line[-1])
    line[-1] = changed_email_line

    if len(line) > 7 and line[-1] == '':
        line.pop(-1)


dictionary = {}
raw_dict = {}
raw_copy = {}
contact_line = contacts_list[0]
name_list = []
for line in contacts_list[1:]:
    for i in range(len(line)):
        raw_dict[contact_line[i]] = line[i]
    if (line[0], line[1]) in dictionary.keys():
        raw_copy[line[0], line[1]] = raw_dict
        for key, value in raw_copy.items():
            for keys, values in value.items():
                if values:
                    dictionary[line[0], line[1]][keys] = values
    else:
        dictionary[line[0], line[1]] = raw_dict
        name_list.append((line[0], line[1]))
    raw_dict = {}

contacts = []
fixed_contacts = [contacts_list[0]]
for line in name_list:
    contacts.append(dictionary[line])


for i in range(len(contacts)):
    fixed_contacts.append([contacts[i]['lastname'], contacts[i]['firstname'], contacts[i]['surname'],
                           contacts[i]['organization'], contacts[i]['position'], contacts[i]['phone'],
                           contacts[i]['email']])


# TODO 2: сохраните получившиеся данные в другой файл
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(fixed_contacts)
