import sys
input = sys.stdin.readline

num = int(input())
time = list(map(int, input().split()))
res = 0
time.sort()

for i in range(num):
    for j in range(i + 1):
        res += time[j]

print(res)