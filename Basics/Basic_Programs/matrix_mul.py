table_row = 3

table = [[0 for i in range(table_row)] for j in range(table_row)]
table2 = [[0 for i in range(table_row)] for j in range(table_row)]
table3 = [[0 for i in range(table_row)] for j in range(table_row)]
count = 0

for i in range(table_row):
    for j in range(table_row):
        table[i][j] = count
        count += 1
        table2[i][j] = count
        count += 1

print("table 1 :\n")
for row in table:
    print(row)

print()

print("table 2 :\n")
for row in table2:
    print(row)

print()

for i in range(table_row):
    for j in range(table_row):
        table3[i][j] = table[i][j] + table2[i][j]

print("added table :\n")

for row in table3:
    print(row)

print()

table3 = [[0 for i in range(table_row)] for j in range(table_row)]

for i in range(table_row):
    for j in range(table_row):
        for k in range(table_row):
            table3[i][j] += table[i][k] * table2[k][j]

print("multiplied table :\n")

for row in table3:
    print(row)