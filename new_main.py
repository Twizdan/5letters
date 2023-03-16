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
    temp = temp[temp.str.contains(pattern)].reset_index(drop=True)
    if temp.shape[0] > 0:
        coefficients = temp.str.split("", expand=True).drop([0, 6], axis=1)
        for i in range(5):
            for j in range(coefficients.shape[0]):
                coefficients[i + 1][j] = mas[i][str(coefficients[i + 1][j])]
        coefficients = coefficients.sum(axis=1)
        temp = pd.DataFrame(temp)
        temp[1] = coefficients
        temp = temp.sort_values(by=1, ascending=False)
    return temp


if __name__ == '__main__':
    data = pd.read_csv("5letters.csv", index_col=0)["0"]
    z = data.str.split("", expand=True).drop([0, 6], axis=1)
    mas = [0] * 5
    for i in range(5):
        mas[i] = (z[i + 1].value_counts(normalize=True))
    good = '1'
    while len(good) != 0:
        good = input('Напишите найденные буквы, ненайденные буквы поставьте точкой: ').lower()
        maybe = input('Напишите буквы не на своем месте: ').lower()
        bad = input('Напишите плохие буквы: ').lower()
        print(find(good, maybe, bad))
        print()
