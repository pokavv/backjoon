import sys
import math

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    # 두 원의 중심이 같을 때
    if x1 == x2 and y1 == y2:
        if r1 == r2: # 반지름이 같음 (동일한 원)
            print(-1)
        else: # 반지름 다르면 영원히 만나지 않음
            print(0)
    
    # 두 원의 중심이 다를 때
    else:
        if abs(r1 - r2) == distance or r1 + r2 == distance: # 내접원 or 외접원
            print(1)
        elif abs(r1 - r2) < distance < r1 + r2: # 두 점에서 만날 때
            print(2)
        else: # 만나지 않음
            print(0)