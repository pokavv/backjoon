num1, num2 = map(int, input().split())
num_list = []

for i in range(1, num1 + 1):
    if num1 % i == 0:
        num_list.append(i)

if len(num_list) >= num2:
    print(num_list[num2 - 1])
else:
    print(0)