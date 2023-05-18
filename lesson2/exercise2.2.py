main_str =input('Введите строку...')
str1 = main_str[1::2]
str2 = main_str[::2]
print('Введена строка ', '"', main_str, '"', sep='', end='  ')
print(str1, str2, sep='     ', end='\n!!!')