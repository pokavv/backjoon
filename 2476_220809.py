player = int(input())

for i in range(player):
    a, b, c = map(int, input().split())
    dice = [a, b, c]
    money = []

    if a == b and b == c and a == c:
        money.append(10000 + (a * 1000))
    elif a == b:
        money.append(1000 + (a * 100))
    elif a == c:
        money.append(1000 + (a * 100))
    elif b == c:
        money.append(1000 + (b * 100))
    else:
        money.append(max(a, b, c) * 100)

print(max(money))