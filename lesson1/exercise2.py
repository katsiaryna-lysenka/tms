my_string = 'aaaaaBccBddBeeBffBggB'
result = my_string[5::3]
print(result)


my_string = 'AAAABBBBCCCCDDDDFFFF'
new_string1 = my_string[:4]
new_string2 = my_string[4:8]
new_string3 = my_string[8:12]
new_string4 = my_string[12:16]
new_string5 = my_string[16:]
result = new_string1[:] + new_string2[:] + new_string3[:] + new_string4[:] + new_string5[:]
print(new_string1, new_string2, new_string3, new_string4, new_string5, result)


string = "PYTHON"
new_string = string[::1]
print(new_string)