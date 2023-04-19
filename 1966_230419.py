from collections import deque
import sys
input = sys.stdin.readline

for i in range(int(input())):
    n, m = map(int, input().split())
    qu = deque(list(map(int, input().split())))
    cnt = 0
    
    while qu:
        max_val = max(qu)
        front_output = qu.popleft()
        m -= 1
        
        if max_val == front_output:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        
        else:
            qu.append(front_output)
            if m < 0:
                m = len(qu) - 1

####################################

import sys

printer_list = []

for _ in range(int(input())):
    n, m = map(int, input().split())
    printer_list = list(enumerate(list(map(int, input().split()))))
    priority = printer_list[m]
    cnt = 0
    
    while len(printer_list):
        max_val = max([i[1] for i in printer_list])
        if printer_list[0][1] == max_val:
            front_output = printer_list.pop(0)
            cnt += 1
            
            if front_output == priority:
                print(cnt)
                break
        
        else:
            front_output = printer_list.pop(0)
            printer_list.append(front_output)