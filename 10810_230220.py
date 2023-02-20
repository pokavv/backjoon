import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = [0] * (N + 1)

for _ in range(M):
    i, j, k = map(int, input().split())
    for ball in range(i, j+1):
        basket[ball] = k

for ball in range(1, N+1):
    print(basket[ball], end=' ')