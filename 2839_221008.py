sugar = int(input())
bag = 0

while sugar >= 0:
    if sugar % 5 == 0:
        bag += (sugar // 5)
        print(bag)
        break
    # 5의 배수 될떄까지 loop
    sugar -= 3
    bag += 1
else:
    print(-1)