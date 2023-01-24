import sys
import math
input = sys.stdin.readline

for _ in range(int(input())):
    # starting point, ending point
    start_x, start_y, end_x, end_y = map(int, input().split())
    
    # entry, exit count
    cnt = 0
    
    # planetary sys
    for _ in range(int(input())):
        planet_x, planet_y, sys_radius = map(int, input().split())
        start_distance = math.sqrt(((start_x - planet_x) ** 2) + ((start_y - planet_y) ** 2))
        end_distance = math.sqrt(((planet_x - end_x) ** 2) + ((planet_y - end_y) ** 2))
        

        if start_distance < sys_radius and end_distance < sys_radius:
            pass
        elif start_distance < sys_radius:
            cnt += 1
        elif end_distance < sys_radius:
            cnt += 1
    
    print(cnt)