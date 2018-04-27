
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]

t = [ [row[i] for row in matrix] for i in range(5)]
print(t)

transposed = []
for i in range(5):
    transposed.append(list(row[i] for row in matrix))

print(transposed)

x = [1,2,3]
y = [4,5,6]

print( list(zip(x,y)) )

print(list(zip(*matrix) ))

print(*matrix)