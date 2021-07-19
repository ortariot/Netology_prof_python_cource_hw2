from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
#   for line in rows:
#       print(line)
    contacts_list = list(rows)
    # pprint(contacts_list)
#   print(rows)


# firstname_pattern = re.compile()
# lastname_pattern = re.compile()
# surname_pattern = re.compile()
phone_template = r'(\+7|8)?(\s*|-)\(?(\d+)\)?(\s*|\s?|-)' + \
    r'(\d{3})(\-|\s*)(\d{2})(\-|\s*)*(\d{2})(\s\(?)?(\доб.\s*\d+)?\)?'

phone_pattern = re.compile(phone_template)
email_pattern = re.compile(r'\d+')
organization_pattern = re.compile(r'\d+')
position_pattern = re.compile(r'\d+')


def name_normalaze(name):
    while(len(name) < 3):
        name.append('')
    return name


def phone_normalaze(phone):
    return re.sub(phone_template, r'+7(\3)-\5-\7-\9 \11', phone)
   


out = []
for line in contacts_list[1:]:
    name = ' '.join(line[:3]).strip().split(' ')
    name = name_normalaze(name)
    organization = [line[3]]
    position = [line[4]]
    phone = [phone_normalaze(line[5])]
    email = [line[6]]

    print(name + organization + position + phone + email)

    
    for item in line:
        
        num = phone_pattern.search(item)
        if num:
            out.append(item)


# print(contacts_list[:1] + out)


# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)


# regex_num = re.compile('\d+')  
# item = "num num opa opa"
# s = regex_num.search(item)

# if s :
#     print("ura")

# print(s)

