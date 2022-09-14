n, m = map(int, input().split())
num = list(map(int, input().split()))
res = 0

for i in range(n):
    for j in range(i + 1, n):
        for q in range(j + 1, n):
            combin = num[i] + num[j] + num[q]
            if combin <= m:
                res = max(res, combin)

print(res)