import sys
input = sys.stdin.readline

list_a = [1, 3, 5, 7, 8, 10, 12]
list_b = [4, 6, 9, 11]

for _ in range(int(input())):
    res = ['No', 'No']
    
    a, b = map(int, input().split())
    if a > 0 and a <= 12:
        if a in list_a and b <= 31 and b > 0:
            res[0] = 'Yes'
        elif a in list_b and b <= 30 and b > 0:
            res[0] = 'Yes'
        elif a == 2 and b <= 29 and b > 0:
            res[0] = 'Yes'
    if a >= 0 and a <= 23:
        if b <= 59:
            res[1] = 'Yes'
    print(res[1], res[0])