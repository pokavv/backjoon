num_sum = 0
for i in list(map(int, input().split())):
    num_sum += i ** 2
print(num_sum % 10)