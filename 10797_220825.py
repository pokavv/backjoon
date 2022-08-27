date_unit = int(input())
car_num = map(int, input().split())
val = 0

for i in car_num:
    if i == date_unit:
        val += 1

print(val)