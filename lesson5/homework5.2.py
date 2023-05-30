def my_func(n):
    if n == 1:
        return 1
    return my_func(n - 1) * n

n = int(input())
print(my_func(n))