import sys
input = sys.stdin.readline

for i in range(int(input())):
    num = int(input())
    if num % 2 == 0:
        print('even')
    else:
        print('odd')