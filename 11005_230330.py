import sys
input = sys.stdin.readline

n, b = map(int, input().split())
res = ''

while n != 0:
    tmp = n % b
    if tmp >= 10:
        res += chr(tmp + 55)
    else:
        res += str(tmp)
    n //= b

print(res[::-1])