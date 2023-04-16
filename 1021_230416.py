from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
position = list(map(int, input().split()))
dq = deque([i for i in range(1, n + 1)])
cnt = 0

for i in position:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq) / 2:
                while dq[0] != i:
                    dq.append(dq.popleft())
                    cnt += 1
            else:
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    cnt += 1

print(cnt)

########################################################

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
position = list(map(int, input().split()))
dq = [i for i in range(1, n + 1)]
cnt = 0

for i in range(m):
    dq_len = len(dq)
    dq_index = dq.index(position[i])
    
    if dq_index < dq_len - dq_index:
        while True:
            if dq[0] == position[i]:
                del dq[0]
                break
            else:
                dq.append(dq[0])
                del dq[0]
                cnt += 1
    else:
        while True:
            if dq[0] == position[i]:
                del dq[0]
                break
            else:
                dq.insert(0, dq[-1])
                del dq[-1]
                cnt += 1

print(cnt)