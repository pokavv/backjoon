from collections import deque
import sys

dq = deque()

for _ in range(int(input())):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push_front":
        dq.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        dq.append(cmd[1])
    elif cmd[0] == "pop_front":
        if dq:
            print(dq[0])    
            dq.popleft()
        else:
            print("-1")
    elif cmd[0] == "pop_back":
        if dq:
            print(dq[len(dq) - 1])    
            dq.pop()
        else:
            print("-1")
    elif cmd[0] == "size":
        print(len(dq))
    elif cmd[0] == "empty":
        if dq:
            print("0")
        else:
            print("1")
    elif cmd[0] == "front":
        if dq:
            print(dq[0])
        else:
            print("-1")
    elif cmd[0] == "back":
        if dq:
            print(dq[len(dq) - 1])
        else:
            print("-1")

################################

import sys
input = sys.stdin.readline

dq = []

for _ in range(int(input())):
    cmd = input().rstrip()
    if ' ' in cmd:
        a, b = cmd.split()
        if a == 'push_front':
            dq.insert(0, b)
        elif a == 'push_back':
            dq.append(b)
    elif 'pop_front' == cmd:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop(0))
    elif 'pop_back' == cmd:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop(-1))
    elif 'size' == cmd:
        print(len(dq))
    elif 'empty' == cmd:
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif 'front' == cmd:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif 'back' == cmd:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])