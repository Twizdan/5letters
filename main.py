# Создали файл со словами только из 5 букв.
import re

f = open(r"singular.txt", encoding='utf-8')
data = f.readlines()
data = [i[:-1] for i in data if len(i) == 6]
f.close()

flag = " "
while flag.lower() != "нет":
    data_probably = []
    data_guessed = []
    data_without_bad = []
    data_almost_guessed = []

    user_input_good_letters = input('Введите "хорошие" буквы: ').lower()
    user_input_bad_letters = input('Введите "плохие" буквы: ').lower()
    user_input_guessed_letters = input("Введите буквы по местам, на которых они стоят. Пример: **И*Д ").\
        replace("*", ".").lower()
    user_input_bad_guessed_letters_list = []

    counter = input('Ещё масочку для неверных? Для конца напишите "0".')
    if counter != '0' and counter.isdigit():
        counter = int(counter)
        for i in range(counter):
            print("Введите буквы по местам, на которых они не стоят. Пример: ***Н*")
            user_input_bad_guessed_letters = input().replace("*", ".").lower()
            user_input_bad_guessed_letters_1 = user_input_bad_guessed_letters.replace(".","")
            user_input_bad_guessed_letters = list(user_input_bad_guessed_letters)
            if len(user_input_bad_guessed_letters_1) > 1:
                for i in range(len(user_input_bad_guessed_letters_1)):
                    for j in range(len(user_input_bad_guessed_letters)):
                        if user_input_bad_guessed_letters[j] != ".":
                            m = '.' * (j) + user_input_bad_guessed_letters[j] + '.' * (len(user_input_bad_guessed_letters) - j  - 1)
                            user_input_bad_guessed_letters[j] = "."
                            user_input_bad_guessed_letters_list.append(m)
            else:
                user_input_bad_guessed_letters_list.append("".join(user_input_bad_guessed_letters))
    if user_input_guessed_letters == '':
        user_input_guessed_letters = '.....'
    for i in range(len(data)):
        for j in range(len(user_input_bad_letters)):
            if user_input_bad_letters[j] in data[i]:
                break
        else:
            data_without_bad.append(data[i])

    for i in range(len(data_without_bad)):
        t = 0
        for j in range(len(user_input_good_letters)):
            if user_input_good_letters[j] in data_without_bad[i]:
                t += 1
        if t == len(user_input_good_letters):
            data_probably.append(data_without_bad[i])

    for i in range(len(data_probably)):
        if re.fullmatch(user_input_guessed_letters, data_probably[i]):
            data_guessed.append(data_probably[i])
    for i in range(len(data_guessed)):
        lol = 0
        for j in range(len(user_input_bad_guessed_letters_list)):
            if not re.fullmatch(user_input_bad_guessed_letters_list[j], data_guessed[i]):
                lol += 1
                if lol == len(user_input_bad_guessed_letters_list):
                    data_almost_guessed.append(data_guessed[i])

    print(*data_almost_guessed if len(data_almost_guessed) != 0 else data_guessed)
    print('Продолжаем? Для выхода напишите "нет".')
    flag = input()


