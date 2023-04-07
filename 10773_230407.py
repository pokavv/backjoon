import sys
input = sys.stdin.readline
arr = []

for _ in range(int(input())):
    i = int(input())
    
    if i:
        arr.append(i)
    else:
        arr.pop()

print(sum(arr))