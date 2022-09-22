import sys
input = sys.stdin.readline

for _ in range(int(input())):
    input()
    location = sorted(map(int, input().split()))
    print((location[-1] - location[0]) * 2)