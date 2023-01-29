import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(n) // (factorial(n - k) * factorial(k))) # n!/(n-k)!k!

# 이항계수: 이항식을 이항정리로 전개했을 때 각 항의 계수, 주어진 크기의 조합의 가짓수
# 조합 공식 nCk를 사용하면 구할수 있음 = n!/(n-k)!k!