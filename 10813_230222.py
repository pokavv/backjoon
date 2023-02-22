import sys
input = sys.stdin.readline

N, M = map(int, input().split())
buckets = [str(i + 1) for i in range(N)]

for bucket in range(M):
    i, j = map(int, input().split())
    buckets[i - 1], buckets[j - 1] = buckets[j - 1], buckets[i - 1]

print(' '.join(buckets))