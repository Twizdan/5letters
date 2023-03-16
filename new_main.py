import pandas as pd
import re


# Создаем файл для работы. Оставляем из всего списка слов только слова из 5 букв.
# with open(r"singular.txt", encoding='utf-8') as f:
#     readed_lines = f.readlines()
#     data = pd.Series(readed_lines)
#     data = data.str.replace(r'\W', '')
#     data = data[data.str.len() == 5]
#     data = data.unique()
#     data = pd.Series(data)
#     print(data)
#     data.to_csv("5letters.csv")
#     #data.to_csv("5letters.csv")

def find(good, maybe, bad):
    temp = data[data.str.match(good, flags=re.IGNORECASE)]
    temp = temp.str.replace(rf'[{bad} ]', '', regex=True)
    temp = temp[temp.str.len() == 5]
    pattern = ('(?=.*{})' * len(maybe)).format(*maybe)
    temp = temp[temp.str.contains(pattern)]
    return temp.tolist()


data = pd.read_csv("5letters.csv", index_col=0)["0"]

if __name__ == '__main__':
    good = '1'
    while len(good) != 0:
        good = input('Напишите найденные буквы, ненайденные буквы поставьте точкой: ').lower()
        maybe = input('Напишите буквы не на своем месте: ').lower()
        bad = input('Напишите плохие буквы: ').lower()
        print(*find(good, maybe, bad))
        print()
