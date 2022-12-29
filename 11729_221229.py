# tower of hanoi


def hanoiTower(disks_num, starting_point, midpoint, arrival_point):    
    if disks_num == 1:
        print(starting_point, arrival_point)
        return
    
    # disk n - 1개를 starting_point -> midpoint 이동 (arrival_point는 edge 역할)
    hanoiTower(disks_num - 1, starting_point, arrival_point, midpoint)
    
    # 가장 큰 disk를 arrival_point로 이동
    print(starting_point, arrival_point)
    
    # disk n - 1개를 midpoint -> arrival_point 이동 (start_point는 edge 역할)
    hanoiTower(disks_num - 1, midpoint, starting_point, arrival_point)

# print('n = 1')
# hanoiTower(1, 1, 2, 3)

# print('n = 2')
# hanoiTower(2, 1, 2, 3)

# print('n = 3')
# hanoiTower(3, 1, 2, 3)

# print('n = 4')
# hanoiTower(4, 1, 2, 3)

disks = int(input())
print(2 ** disks - 1) # hanoi formula : (2 ** n) - 1
hanoiTower(disks, 1, 2, 3)