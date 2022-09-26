import sys
input = sys.stdin.readline
n, m = map(int, input().split())
bsk = [i + 1 for i in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    bsk = bsk[:a-1] + bsk[a-1:b][::-1] + bsk[b:]

for i in bsk:
    print(i, end=' ')