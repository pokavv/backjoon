num_on_train = []
people_num = 0

for i in range(4):
    off, on = map(int, input().split())
    people_num += on
    people_num -= off
    num_on_train.append(people_num)

print(max(num_on_train))