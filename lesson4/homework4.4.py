x = [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
y = [(3, 3, 3), (2, 2, 2), (1, 1, 1)]
z = [(2, 2, 2), (3, 3, 3), (4, 4, 4)]
x1 = x[0] + x[1] + x[2]
y1 = y[0] + y[1] + y[2]
z1 = z[0] + z[1] + z[2]
x2, y2, z2 = list(x1), list(y1), list(z1)
result = [n1 * n2 * n3 for n1, n2, n3 in zip(x2, y2, z2)]
print(result)