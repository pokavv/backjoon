import sys
input = sys.stdin.readline

n, k = map(int, input().split())
circle = [i for i in range(1, n + 1)]
josephus_arr = []
tmp = k - 1

while circle:
    josephus_arr.append(circle.pop(tmp))
    if circle:
        tmp = ((tmp - 1) + k) % len(circle)

print(f'<{", ".join(map(str, josephus_arr))}>')