from pprint import pprint
import csv
import re

def name_normalaze(name):
    while(len(name) < 3):
        name.append('')
    return name

def phone_normalaze(phone, phone_template):
    return re.sub(phone_template, r'+7(\3)-\5-\7-\9 \11', phone)
   
def contact_book_cleaner(input_list, pt):
    out = {}
    table_head = input_list[0] 
    for line in input_list[1:]:
        line = name_normalaze(' '.join(line[:3]).strip().split(' ')) + line[3:]
        line[5] = phone_normalaze(line[5], pt)
        mod_line = {key : value for key, value in dict(zip(table_head, line)).items() if value != "" }
        if out.get(mod_line[table_head[0]]):
            out[mod_line[table_head[0]]].update(mod_line)
        else:
            out[mod_line[table_head[0]]] = mod_line
    return [value for value in out.values()]


if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    phone_template = r'(\+7|8)?(\s*|-)\(?(\d+)\)?(\s*|\s?|-)' + \
    r'(\d{3})(\-|\s*)(\d{2})(\-|\s*)*(\d{2})(\s\(?)?(\доб.\s*\d+)?\)?'
    out = contact_book_cleaner(contacts_list, phone_template)
    pprint(out)

    with open("phonebook.csv", "w") as f:
        fieldnames = contacts_list[0]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out)



