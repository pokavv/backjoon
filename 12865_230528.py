import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
bag = [(0, 0)]
dp = [[0] * (k + 1) for _ in range(n + 1)]

for _ in range(n):
    w, v = map(int, input().rstrip().split())
    bag.append((w, v))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w, v = bag[i]
        
        if j >= w:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[i][k])