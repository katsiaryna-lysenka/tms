n = input('Введите строку: ')
str1, str2, str3, str4 = n.split()
with open('test.txt', 'w') as f:
    f.write(str1 + '\n')
    f.write(str2 + '\n')
with open('test.txt', 'a') as f1:
    f1.write(str3 + '\n')
    f1.write(str4 + '\n')

