import sys
input = sys.stdin.readline

# (a, b)를 입력값으로 받는 리스트를 a position을 기준으로 오름차정렬하는 wire_position_list
wire_ = int(input())
wire_position_list = sorted([list(map(int, input().split())) for _ in range(wire_)])
dp = [1] * wire_

# b position에서 가장 긴 증가하는 부분수열을 구해서 정렬된 wire_position_list의 b position을 뺀다.
for i in range(wire_):
    for j in range(i):
        if wire_position_list[i][1] > wire_position_list[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(wire_ - max(dp))