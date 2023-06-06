def is_number(str):
    if str.isdigit():
        return (f'Вы ввели положительное целое число {str}')
    elif '-' in str:
        str = str[1:]
        if str.isdigit():
            return (f'Вы ввели отрицательное целое число -{str}')
        else:
            try:
                float(str)
                return (f'Вы ввели отрицательное дробное число -{str}')
            except:
                return (f'Вы ввели не корректное число -{str}')
    else:
        try:
            float(str)
            return (f'Вы ввели положительное дробное число {str}')
        except:
            return (f'Вы ввели не корректное число {str}')
str = input('Введите строку: ')
print(is_number(str))
