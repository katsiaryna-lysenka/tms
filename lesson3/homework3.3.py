while True:
    name, age = input(), input()
    if age.isdigit():
        if int(age) <= 0:
            print('Ошибка, повторите ввод')
        elif int(age) < 10:
            print(f"Привет, шкет {name}")
        elif 10 <= int(age) <= 18:
            print(f"Как жизнь {name}?")
        elif 18 < int(age) < 100:
            print(f"Что желаете {name}?")
        else:
            print(f"{name}, вы лжете - в наше время столько не живут")
    else:
        print('Ошибка, повторите ввод')