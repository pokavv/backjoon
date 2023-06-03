import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sum_arr = [[0] * (n + 1)]
td_arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(n):
    sum_arr.append([0] + [int(i) for i in input().split()])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        td_arr[i][j] = td_arr[i - 1][j] + td_arr[i][j - 1] - td_arr[i - 1][j - 1] + sum_arr[i][j]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    res = td_arr[x2][y2] - td_arr[x1 - 1][y2] - td_arr[x2][y1 - 1] + td_arr[x1 - 1][y1 - 1]
    print(res)