# 기약분수 : 분자와 분모의 최대공약수를 분자, 분모에 각각 나눔

import sys
input = sys.stdin.readline

ring_num = int(input())
rings = list(map(int, input().split()))

# 유클리드 호제법: mod 연산 반복 > 나머지가 0일때 최대공약수

def gcd(a, b):
    while b > 0:
        mod_res = a % b
        a, b = b, mod_res
    return a

for i in range(1, ring_num):
    rings_gcd = gcd(rings[0], rings[i])
    print(f'{rings[0] // rings_gcd}/{rings[i] // rings_gcd}')