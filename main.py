
import re
import csv

def correct_full_names(data):
    for i in range (1, len(data)):
        fio = data[i][:3]
        fio = ' '.join(fio).rstrip().split()
        for j in range(0, len(fio)):
            data[i][j] = fio[j]
    return data

def correct_phone_numbers(data):
    pattern = r"(\+7|8)\s?[\(]?(\d{3})[\)]?\s?[-]?(\d{3})[-]?(\d{2})[-]?(\d{2})\s?[\(]?(доб.)?\s?(\d*)?[\)]?"
    sub = r"+7(\2)\3-\4-\5 \6\7"
    for i in range(1, len(data)):
        result = re.sub(pattern, sub, data[i][5])
        data[i][5] = result.strip()
    return data

def find_dublicates(data):
    unique_fio = {}
    for person in data[1:]:
        print(unique_fio)
        fi = person[0] + " " + person[1]
        print(fi)
        if fi not in unique_fio:
            unique_fio[fi] = person[2:]
        else:
            for i in range(5):
                if not unique_fio[fi][i]:
                    unique_fio[fi][i] = person[i+2]
    return unique_fio

def result(data):
    result = []
    for fi, inf in data.items():
        fi = fi.split()
        fi.extend(inf)
        result.append(fi)
    return result


with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

updated_list = correct_full_names(contacts_list)
updated_list = correct_phone_numbers(updated_list)
updated_list = find_dublicates(updated_list)
updated_list = result(updated_list)

with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(updated_list)
