first_name, second_name = input(), input()
second_name, first_name = first_name, second_name
print('!', first_name, ' ! ', second_name, '!', sep='')
print(f'!{first_name} ! {second_name}! ')
print('!{var1} ! {var2}!'.format(var1=first_name, var2=second_name))