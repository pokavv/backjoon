import sys
input = sys.stdin.readline

city = int(input())
load_km = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
res = 0

for i in range(city - 1):
    if min_price > price[i]:
        min_price = price[i]
    
    res += min_price * load_km[i]

print(res)