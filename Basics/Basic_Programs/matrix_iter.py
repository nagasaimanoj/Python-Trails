matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("row-wise")
for i in range(3):
    for j in range(3):
        print(matrix[i][j])

print("col-wise")
for j in range(3):
    for i in range(3):
        print(matrix[i][j])

print("skipping a row")
for i in range(3):
    if i == 1:
        continue
    for j in range(3):
        print(matrix[i][j])


print("skipping a col")
for j in range(3):
    if j == 1:
        continue
    for i in range(3):
        print(matrix[i][j])
