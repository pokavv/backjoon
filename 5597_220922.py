import sys
input = sys.stdin.readline
arr = []

for n in range(1, 31):
    arr.append(n)

for i in range(28):
    i = int(input())
    arr.remove(i)

print(min(arr))
print(max(arr))