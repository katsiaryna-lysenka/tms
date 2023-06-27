class MyException(Exception):
    pass

def calculator():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        operation = input("Введите операцию (+,-,*,/): ")
        if operation == "+":
            print(a + b)
        elif operation == "-":
            print(a - b)
        elif operation == "*":
            print(a * b)
        elif operation == "/":
            print(a / b)
        else:
            raise MyException("Некорректная операция")
    except ZeroDivisionError:
        print("Деление на ноль невозможно")
    except ValueError:
        print("Некорректный ввод")
    except MyException as e:
        print(e)


calculator()
