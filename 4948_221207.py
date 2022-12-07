# 베르트랑 공준: 임의의 자연수 n에 대하여 n보다 크고 2n보다 작거나 같은 소수는 적어도 하나 존재함
# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.
# 어떤 자연수 n이 소수임을 판정하기 위해선 root n까지의 수 중 1을 제외하고 그 자연수의 약수가 있는지 확인

import math

def check(val):
    if val == 1:
        return True
    else:
        for i in range(2, int(math.sqrt(num))+1): # sqrt(): python 제곱근 함수
            if val % i == 0:
                return False
    return True

value = list(range(123456*2))
prime_number = list()

for num in value:
    if check(num):
        prime_number.append(num)

while True:
    n = int(input())
    cnt = 0
    
    if n == 0:
        break
    
    for i in prime_number:
        if n < i <= n * 2:
            cnt += 1
    print(cnt)

'''
-- timeout

def sosu(num):
    cnt = 0
    for i in range(num+1, 2*num):
        cnt += 1
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                cnt -= 1
                break
    return cnt

while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print(1)
    else:
        print(sosu(n))
'''