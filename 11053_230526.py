import sys
input = sys.stdin.readline

seq_len = int(input())
subsequence = list(map(int, input().split()))
dp = [0 for _ in range(seq_len)]

for i in range(seq_len):
    for j in range(i):
        if subsequence[i] > subsequence[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    #         print(dp)
    #         print('---')
    # print('====')