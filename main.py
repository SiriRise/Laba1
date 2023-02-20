#Восьмиричные числа не превышающие 2048 в десятичной системе счисления.
#Выводит на экран нечетные числа, использующие не менее К разных цифр.
#Список используемых цифр выводится отдельно прописью.

slovar = {"0": "ноль", "1": "один", "2": "два", "3": "три", "4": "четыре", "5": "пять", "6": "шесть", "7": "семь"}

try:
    buffer_len = 1
    work_buffer = ""
    with open("text.txt", "r") as file:
        buffer = file.read(buffer_len)
        if not buffer:
            print("Файл пуст")
            exit()
        print("Введите количество разных цифр")
        diff_number = int(input())
        good = 0
        while buffer:
            while buffer >= "0" and buffer <= "7":
                if buffer >= "0" and buffer <= "7":
                    work_buffer += buffer
                buffer = file.read(buffer_len)
            if len(work_buffer) > 0:
                f_b = True
                for i in range (len(work_buffer)):
                    if work_buffer[i] == 9 or work_buffer == 8:
                        f_b = False
                if len(work_buffer)> 1:
                    if len(work_buffer) < 5 and int(work_buffer) % 2 != 0 and int(work_buffer,8) <= 2048:
                        if len(set(work_buffer)) >= diff_number:
                            good += 1
                            print(work_buffer)
                            num = ("".join(sorted(set(work_buffer), key=work_buffer.index)))
                            for j in range (len(num)):
                                print(slovar[(num[j])], end=" ")
                            print()
            work_buffer = ""
            buffer = file.read(buffer_len)
        if good == 0:
            print('нет подходящих чисел')
except FileNotFoundError:
    print('Файл не найден')
