import sys

num = list(map(int, sys.stdin.readline().split()))

for i in range(5):
    for j in range(4):
        if num[j] > num[j + 1]:
            tmp = num[j]
            num[j] = num[j + 1]
            num[j + 1] = tmp
            print(*num)