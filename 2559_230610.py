# 시간초과
import sys
input = sys.stdin.readline

# n : 온도를 측정한 전체 날짜의 수
# k : 합을 구하기 위한 연속적인 날짜의 수
n, k = map(int, input().split())
daily_temp = list(map(int, input().split()))
temp_sum = []

for i in range(len(daily_temp)):
    if i + k - 1 == len(daily_temp) - 1:
        temp_sum.append(sum(daily_temp[i:i + k]))
        break
    temp_sum.append(sum(daily_temp[i:i + k]))

print(max(temp_sum))

#####################################################

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
daily_temp = list(map(int, input().split()))
k_temp = [sum(daily_temp[:k])] # k_temp : k일까지 온도의 합

for i in range(1, len(daily_temp) - k + 1):
    part_sum = k_temp[-1] + daily_temp[i + k - 1] - daily_temp[i - 1]
    k_temp.append(part_sum)

print(max(k_temp))