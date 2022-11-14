#################
'''
에라토스테네스의 체: 소수판별 알고리즘
'''
#################

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

m, n = map(int, input().split())

for i in range(m, n + 1):
    if isPrime(i):
        print(i)


def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)