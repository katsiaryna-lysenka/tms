from random import randint


def fill_list(minimum, maximum, amount, empty_list):
    for i in range(amount):
        empty_list.append(randint(minimum, maximum))


def analysis(from_list, to_dict):
    for i in from_list:
        if i in to_dict:
            to_dict[i] += 1
        else:
            to_dict[i] = 1


lst = []
dct = {}

mn = int(input('Введите число минимум: '))
mx = int(input('Введите число максимум: '))
qty = int(input('Введите количество элементов: '))

fill_list(mn, mx, qty, lst)
analysis(lst, dct)

for item in sorted(dct):
    print(f"'{item}': {dct[item]}")
