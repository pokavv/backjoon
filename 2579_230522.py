import sys
input = sys.stdin.readline

stair_num = int(input())
stair = [int(input()) for _ in range(stair_num)]
dp = [0] * stair_num

if len(stair) <= 2:
    print(sum(stair))
else:
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]

    for i in range(2, stair_num):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])
    
    print(dp[-1])