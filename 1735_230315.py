import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

aja, amo = map(int, input().split())
bja, bmo = map(int, input().split())
gcd_num = gcd((aja * bmo) + (bja * amo), amo * bmo)

print(((aja * bmo) + (bja * amo)) // gcd_num,
      (amo * bmo) // gcd_num)