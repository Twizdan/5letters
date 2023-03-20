import pandas as pd
import re


def find(good, maybe, bad):
    try:
        data = pd.read_csv("words_coefs.csv", index_col=0)
        temp = data[data["0"].str.match(good, flags=re.IGNORECASE)]
        temp["0"] = temp["0"].str.replace(rf'[{bad} ]', '', regex=True)
        temp = temp[temp["0"].str.len() == 5]
        pattern = ('(?=.*{})' * len(maybe)).format(*maybe)
        temp = temp[temp["0"].str.contains(pattern)].reset_index(drop=True)
        if temp.shape[0] == 0:
            return "Не найдено ни одного слова."
        temp.columns = ["Слово", "Значение"]
        return temp.head(20).to_string(index=False)
    except:
        return "Вы ввели лишние символы, попробуйте ввести заново"

def calculate_coefs():
    data = pd.read_csv("words_coefs.csv", index_col=0)
    mas = pd.read_csv("coefs.csv", index_col=0)
    temp = data[data["0"].str.match(good, flags=re.IGNORECASE)]
    coefficients = temp.str.split("", expand=True).drop([0, 6], axis=1)
    for i in range(5):  # переписать
        for j in range(coefficients.shape[0]):
            coefficients[i + 1][j] = mas[str(i)][str(coefficients[i + 1][j])]
    coefficients = coefficients.sum(axis=1).round(3)
    temp = pd.DataFrame(temp)
    temp[1] = coefficients
    temp = temp.sort_values(by=1, ascending=False)
    coef_sum = temp[1].sum()
    temp[1] = (temp[1] / coef_sum).round(3) * 100

def file_creator(name: str, endname: str):
    with open(name, encoding='utf-8') as f:
        readed_lines = f.readlines()
        data = pd.Series(readed_lines)
        data = data.str.replace(r'\W', '')
        data = data[data.str.len() == 5]
        data = data.unique()
        data = pd.Series(data)
        print(data)
        data.to_csv(endname)


if __name__ == '__main__':
    good = '1'
    while len(good) != 0:
        good = input('Напишите найденные буквы, ненайденные буквы поставьте точкой: ').lower()
        maybe = input('Напишите буквы не на своем месте: ').lower()
        bad = input('Напишите плохие буквы: ').lower()
        print(find(good, maybe, bad))
        print()
