min_num = int(input())
max_num = int(input())
prime_num = []

for i in range(min_num, max_num + 1):
    if i != 1:
        check_num = True
        for j in range(2, i):
            if i % j == 0:
                check_num = False
                break
        if check_num:
            prime_num.append(i)
if len(prime_num) == 0:
    print(-1)
else:
    print(sum(prime_num))
    print(prime_num[0])