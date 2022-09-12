import sys
a, b = map(int, sys.stdin.readline().split())
maxn = max(a, b)
minn = min(a, b)

# a와 b사이의 합을 구하는 공식
num_sum = (a + b) * (maxn - minn + 1) / 2

print(int(num_sum))