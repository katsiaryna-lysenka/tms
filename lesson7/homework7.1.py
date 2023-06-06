n = int(input('Введите число: '))
result = lambda n: n % 2
if result(n) == 0:
    print('Чётное')
else:
    print('Нечётное')
