n = int(input())
table = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            table[i][j] = 1

res = 0
for row in table:
    res += row.count(1)
print(res)