import sys
input = sys.stdin.readline

total_price = int(input())

for i in range(int(input())):
    price, cnt = map(int, input().split())
    total_price -= price * cnt

if total_price == 0:
    print('Yes')
else:
    print('No')