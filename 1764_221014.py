import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nlist = []
mlist = []

for _ in range(n):
    nlist.append(input().strip())
for _ in range(m):
    mlist.append(input().strip())

intersection_val = list(set(nlist) & set(mlist))
print(len(intersection_val))

for i in sorted(intersection_val):
    print(i)