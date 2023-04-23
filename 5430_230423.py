from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p = input().strip()
    n = int(input())
    arr = input().strip()
    
    dq = deque(arr[1:-1].split(','))
    if n == 0:
        dq = deque()
    
    tmp = 1
    
    reverse_op = 0
    for i in range(len(p)):
        if p[i] == 'R':
            reverse_op += 1
        elif p[i] == 'D':
            if len(dq) == 0:
                print('error')
                tmp = 0
                break
            else:
                if reverse_op % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()
    
    if tmp == 0:
        continue
    else:
        if reverse_op % 2 == 0:
            print('[' + ','.join(dq) + ']')
        else:
            dq.reverse()
            print('[' + ','.join(dq) + ']')