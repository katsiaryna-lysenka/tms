first = 2
second = first
third = first
print(id(first), id(second), id(third), end='\n\n')



fourth = [1, 2, 3]
fifth = [1, 2, 3]
print(id(fourth), id(fifth), end='\n\n')



second = float(first)
third = float(first)
fourth = [1, 2, 3]
fifth = [1, 2, 3]
print(id(first), id(second), id(third), id(tuple(fourth)), id(tuple(fifth)), end='\n\n')


