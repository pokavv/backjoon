import sys
input = sys.stdin.readline

n = int(input())
nums = map(int, input().split())
check_num = int(input())

cnt = 0
for i in nums:
    if i == check_num:
        cnt += 1

print(cnt)