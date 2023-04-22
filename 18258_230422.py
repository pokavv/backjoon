import sys
from collections import deque
input = sys.stdin.readline
dq = deque()

for _ in range(int(input())):
    st = input().split()
    
    if st[0] == 'push':
        dq.append(st[1])
    elif st[0] == 'pop':
        if not dq:
            print(-1)
        else:
            print(dq.popleft())
    elif st[0] == 'size':
        print(len(dq))
    elif st[0] == 'empty':
        if not dq:
            print(1)
        else:
            print(0)
    elif st[0] == 'front':
        if not dq:
            print(-1)
        else:
            print(dq[0])
    elif st[0] == 'back':
        if not dq:
            print(-1)
        else:
            print(dq[-1])