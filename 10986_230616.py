import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
part_sum = [0] * (n + 1)
dp = [0] * (m + 1)

for i in range(n):
    part_sum[i + 1] = (part_sum[i] + arr[i]) % m
    dp[part_sum[i + 1]] += 1

res = dp[0]

for i in range(m + 1):
    res += (dp[i] * (dp[i] - 1)) // 2

print(res)