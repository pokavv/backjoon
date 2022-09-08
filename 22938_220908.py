# 두 원의 반지름의 합이 두 원의 중심과의 거리보다 크면 겹치고, 작으면 안 겹침

x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

# 두 원의 중심거리: 루트((x1 - x2)**2 + (y1 - y2)**2)
d = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)

if (r1 + r2) ** 2 > d:
# 중심거리 식에서 루트를 씌우는 대신 두 원의 반지름 합에 제곱을 해줌
    print('YES')
else:
    print('NO')