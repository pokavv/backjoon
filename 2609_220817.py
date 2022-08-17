a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
# a와 b의 최대공약수 : b와 r(a % b)의 최대공약수와 같다

def lcm(a, b):
    return a * b // gcd(a, b)
# a와 b의 최소공배수 : a * b를 (a,b의 최대공약수)로 나눈다

print(gcd(a, b)) # 최대공약수
print(lcm(a, b)) # 최소공배수