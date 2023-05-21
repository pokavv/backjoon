import sys
input = sys.stdin.readline

seq_1 = ' ' + str(input().rstrip())
seq_2 = ' ' + str(input().rstrip())
dp = [[0] * len(seq_2) for _ in range(len(seq_1))]

for i in range(1, len(seq_1)):
    for j in range(1, len(seq_2)):
        if seq_1[i] == seq_2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])