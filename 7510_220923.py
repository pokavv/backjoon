import sys
input = sys.stdin.readline

for i in range(int(input())):
    num = sorted(map(int, input().split()))
    
    if num[0] ** 2 + num[1] ** 2 == num[2] ** 2:
        print(f'Scenario #{i + 1}:')
        print('yes\n')
    else:
        print(f'Scenario #{i + 1}:')
        print('no\n')