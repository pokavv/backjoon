import sys
input = sys.stdin.readline

n1 = int(input())
n2 = int(input())
n3 = int(input())

n = n1 * n2 * n3

for i in range(10):
    print(str(n).count(str(i)))