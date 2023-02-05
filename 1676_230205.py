num = int(input())

def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

cnt = 0
tmp = str(factorial(num))[::-1]

for i in tmp:
    if i == '0':
        cnt += 1
    else:
        break

print(cnt)

'''
팩토리얼에서 0이 늘어나는 순간은 10(2*5)이 곱해지는 순간으로 5의 개수를 찾아야 함
5, 25, 125 (625부터는 500 범위 밖)

///////////////////////////

import sys
input = sys.stdin.readline

num = int(input())
cnt = 0

while num >= 5:
    cnt += num // 5
    num //= 5

print(cnt)

////////////////////////////

N = int(input())
print(N//5 + N//25 + N//125)
'''