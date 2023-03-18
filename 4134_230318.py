import sys
input = sys.stdin.readline

def isPrime(n):
    if n == 0 or n == 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

for t in range(int(input())):
    n = int(input())
    
    while not isPrime(n):
        n += 1
    
    if isPrime(n):
        print(n)