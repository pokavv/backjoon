import sys
input = sys.stdin.readline

cnt = 1
stack = []
operator = []
TorF = True

for i in range(int(input())):
    num = int(input())
    
    while cnt <= num:
        stack.append(cnt)
        operator.append('+')
        cnt += 1
    
    if stack[-1] == num:
        stack.pop()
        operator.append('-')
    else:
        TorF = False
        break

if TorF == False:
    print('NO')
else:
    for i in operator:
        print(i)