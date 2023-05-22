n = int(input())
summ = 0
for i in range(1, n + 1):
    summ += i**3
print(summ)

n = int(input())
i, summ = 0, 0
while i < n + 1:
    summ += i**3
    i += 1
print(summ)