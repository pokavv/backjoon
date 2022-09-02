num = int(input())
cnt = 0

while num != 1:
    if num % 2 == 0:
        num = num // 2
    else:
        num = num + 1
    cnt += 1

print(cnt)