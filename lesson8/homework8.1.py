num1 = b'r\xc3\xa9sum\xc3\xa9'
num2 = num1.decode('utf-8')
print(num2)
num3 = num2.encode('Latin1')
print(num3)
num4 = num3.decode('Latin1')
print(num4)
