import sys
input = sys.stdin.readline

N = int(input())
tmp = []
nums = sorted([int(input()) for _ in range(N)])

for i in range(1, N):
    tmp.append(nums[i] - nums[i - 1])

# 유클리드 호제법
def uclid(a, b):
    while b > 0:
        a, b = b, a % b
    return a

gcd = tmp[0]
for idx in range(1, len(tmp)):
    gcd = uclid(gcd, tmp[idx])

gcd_set = set()
for i in range(2, int(gcd ** 0.5) + 1):
    if gcd % i == 0:
        gcd_set.add(i)
        gcd_set.add(gcd // i)

gcd_set.add(gcd)
print(*sorted(list(gcd_set)))