import sys
num = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
tmp = 0
res = []

for i in range(1, num):
    if arr[i] > arr[i - 1]:
        tmp += arr[i] - arr[i - 1]
    # i == num - 1이고 오르막길이면 res에 추가되지 않기에 if문 생성
        if i == num - 1:
            res.append(tmp)
    else:
        res.append(tmp)
        tmp = 0

print(max(res))