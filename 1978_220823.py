input_num = int(input())
list_num = map(int, input().split())
prime_num = 0

for i in list_num:
    check_num = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                check_num += 1
        if check_num == 0:
            prime_num += 1
print(prime_num)