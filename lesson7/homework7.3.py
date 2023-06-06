n = ('tpt', 'smile', 'dance', 'ghthg', 'end')
result = filter(lambda x: x[::-1] == x, n)
print(list(result))