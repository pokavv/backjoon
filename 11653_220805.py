num = int(input())
min = 2

while num != 1:
    if num % min == 0:
        print(min)
        num = num // min
    else:
        min += 1