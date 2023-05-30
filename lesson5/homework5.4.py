import time
from datetime import timedelta, datetime
n = int(input('Введите число: '))
def func(n):
    for i in range(1, n):
        print(datetime.now() + timedelta(seconds=1))
        n += 1
    return datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
print(func(n))
