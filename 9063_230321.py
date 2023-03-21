import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
min_x, min_y, max_x, max_y = a, b, a, b

for i in range(n - 1):
    x, y = map(int, input().split())
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)

print((max_x - min_x) * (max_y - min_y))