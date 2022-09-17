import sys
cnt, res = 1, 1
num = int(sys.stdin.readline())

for i in range(num):
    res += cnt
    if i % 2 == 0:
        cnt += 1

print(res)