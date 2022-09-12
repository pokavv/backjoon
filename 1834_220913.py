import sys
num = int(sys.stdin.readline())
arr = []

for i in range(num + 1, num ** 2, num + 1):
    if i % num == i // num:
        arr.append(i)

print(sum(arr))