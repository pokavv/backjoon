import sys
input = sys.stdin.readline
arr = []

for i in range(7):
    num = int(input())
    if num % 2 != 0: arr.append(num)
if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)