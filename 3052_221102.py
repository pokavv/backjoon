import sys
input = sys.stdin.readline
arr = []

for i in range(10):
    arr.append((int(input())) % 42)

arr = set(arr)
print(len(arr))