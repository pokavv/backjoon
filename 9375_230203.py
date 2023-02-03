import sys
input = sys.stdin.readline

for _ in range(int(input())):
    clothes_num = int(input())
    clothes = {}
    
    for _ in range(clothes_num):
        clothes_name, clothes_type = input().split()
        
        if clothes_type not in clothes.keys():
            clothes[clothes_type] = 1
        else:
            clothes[clothes_type] += 1
    
    res = 1
    for i in clothes:
        res *= (clothes[i] + 1)
    
    print(res - 1) # 알몸인 경우 제외