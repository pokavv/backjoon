import sys
input = sys.stdin.readline

n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

'''
num.sort()

for i in num:
    print(i)
'''

for i in range(len(num)):
    for j in range(len(num)):
        if num[i] < num[j]:
            num[i], num[j] = num[j], num[i]

for n in num:
    print(n)