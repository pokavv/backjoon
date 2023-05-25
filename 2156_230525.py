import sys
input = sys.stdin.readline

glass_num = int(input())
wine = [int(input()) for _ in range(glass_num)]
dp = [0] * (glass_num + 1)
dp[0] = wine[0]

print(wine)
print(dp)

# if glass_num > 1:
#     dp[1] = wine[0] + wine[1]
# if glass_num > 2:
#     dp[2] = max(wine[2] + wine[1], wine[2] + wine[0], dp[1])

for i in range(3, glass_num):
    dp[i] = max(dp[i-1], dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i])

print(dp[glass_num-1])

################

# ① 현재 포도주와 이전 포도주를 마시고 전전 포두주는 마시지 않는다. ( wine[i]+wine[i-1]+dp[i-3] )
# ② 현재 포도주와 전전 포도주를 마시고 이전 포도주는 마시지 않는다. ( wine[i]+dp[i-2] )
# ③ 현재 포도주를 마시지 않는다. ( dp[i-1] )

# 이 세 가지 경우로 나눌 수 있다.
# 이 때, 3번케이스의 경우 dp[i-2]+wine[i-1] 로 표기하지 않은 이유는
# dp[i-1]에 해당 케이스를 포함한 최댓값이 저장되어 있기 때문이다.

# https://hongcoding.tistory.com/48