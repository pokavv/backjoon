a, b = map(int, input().split())
min_num = min(a, b)
max_num = max(a, b)
differ_num = max_num - min_num - 1

if min_num == max_num or min_num + 1 == max_num:
    differ_num = 0    
print(differ_num)

for i in range(min_num + 1, max_num):
    print(i, end = ' ')