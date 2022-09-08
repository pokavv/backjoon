num = list(input())
num_sum = 0

for i in range(len(num)):
    num_sum += int(num[i]) ** 5
print(num_sum)