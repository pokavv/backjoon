def d(n):
    n += sum(map(int, str(n)))
    return n

num = set()
for i in range(1, 10001):
    num.add(d(i))

for j in range(1, 10001):
    if j not in num:
        print(j)