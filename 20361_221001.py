import sys
input = sys.stdin.readline

cup, num, loop = map(int, input().split())
arr = []

for i in range(cup):
    arr.append(i + 1)

cup_change = [list(map(int, input().split())) for _ in range(loop)]

for i in range(loop):
    arr[cup_change[i][0] - 1], arr[cup_change[i][1] - 1] = arr[cup_change[i][1] - 1], arr[cup_change[i][0] - 1]

print(arr.index(num) + 1)