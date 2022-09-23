import sys
input = sys.stdin.readline

for _ in range(int(input())):
    num = int(input())
    res = 0
    
    for i in range(1, num):
        if i ** 2 <= num:
            res += 1
        if i ** 2 > num:
            break
    
    print(res)