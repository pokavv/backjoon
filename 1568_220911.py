num = int(input())
res = 0

i = 1
while num > 0:
    if num < i:
        i = 1
    num -= i
    i += 1
    res += 1

print(res)