import sys
input = sys.stdin.readline

for i in range(int(input())):
    num_ship, distance = map(int, input().split())
    res = 0
    
    for j in range(num_ship):
        top_speed, fuel, consumption_rate = map(int, input().split())
        if (fuel / consumption_rate) * top_speed >= distance:
            res += 1
    print(res)