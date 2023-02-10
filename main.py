#Восьмиричные числа не превышающие 2048 в десятичной системе счисления.Выводит на экран нечетные числа, использующие не менее К разных цифр.
#Список используемых цифр выводится отдельно прописью.
import os

slovar = {"0": "ноль", "1": "один", "2": "два", "3": "три", "4": "четыре", "5": "пять", "6": "шесть", "7": "семь"}

def number_by_word(number):
    return slovar[number]

file_name = "text.txt"

try:
    file = open(file_name).read()
except FileNotFoundError:
    print("Файл не обнаружен")
    exit()

if os.stat(file_name).st_size == 0:
    print("Файл пустой")
    exit()

try:
    while True:
        try:
            print("Введите количество разных цифр")
            diff_number = int(input())
        except ValueError:
            print("Вы ввели не цифру")
            continue
        break
    great = 0
    for i in file.split():
        word = 0
        if i.isdigit() == True:
            num = int(i, 8)
            if num <= 2048 and int(i) % 2 != 0:
                if diff_number <= len(set(i)):
                    print(i)
                    great += 1
                    con_line = i
                    con_num = []
                    for j in range(len(set(con_line))):
                        if con_line[j] != " ":
                            con_num.append(con_line[j])
                            print(number_by_word(con_line[j]))
        else:
            word += 1

    if great > 0:
        exit()
    elif great == 0 and word == 0:
        print("Нет подходящих чисел")
    elif word>0 and great == 0:
        print("В файле нет чисел")
except ValueError:
    print("В файле есть не восьмеричные числа")

