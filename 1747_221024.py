import sys
input = sys.stdin.readline

def check_palindrome(n):
    length = len(n) // 2
    for i in range(length):
        if n[i] != n[-i - 1]:
            return False
    return True

def check_primeNumber(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True

n = int(input())
while True:
    if check_palindrome(str(n)) and check_primeNumber(n):
        break
    n += 1

print(n)