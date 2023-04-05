import sys
from collections import defaultdict
input = sys.stdin.readline

dance_log = defaultdict(bool)
dance_log['ChongChong'] = True
res = 1

for _ in range(int(input())):
    a, b = input().split()

    if dance_log[a]:
        if not dance_log[b]:
            dance_log[b] = True
            res += 1
    elif dance_log[b]:
        dance_log[a] = True
        res += 1

print(res)