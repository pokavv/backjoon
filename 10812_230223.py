import sys
input = sys.stdin.readline

n, m = map(int, input().split())
buckets = [num + 1 for num in range(n)]

for _ in range(m):
    begin, end, mid = map(int, input().split())
    buckets[begin - 1:end] = buckets[mid - 1:end] + buckets[begin - 1:mid - 1]

print(*buckets)