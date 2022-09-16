num_max = 0
x, y = 0, 0

for i in range(9):
    row = list(map(int, input().split()))
    if max(row) > num_max:
        num_max = max(row)
        x = i
        y = row.index(num_max)

print(num_max)
print(x + 1, y + 1)