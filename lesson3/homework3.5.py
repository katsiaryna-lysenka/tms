result = True
while result:
    number = 4
    user_number= int(input('Введите ваше число: '))
    if user_number == number:
        print('Верно! Вы угадали')
        result = False
    else:
        print('Попробуйте ещё раз!')