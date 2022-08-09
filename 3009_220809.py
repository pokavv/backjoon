x_coordinate = []
y_coordinate = []

for _ in range(3):
    x, y = map(int, input().split())
    x_coordinate.append(x)
    y_coordinate.append(y)

for i in range(3):
    if x_coordinate.count(x_coordinate[i]) == 1:
        x4 = x_coordinate[i]
    if y_coordinate.count(y_coordinate[i]) == 1:
        y4 = y_coordinate[i]
print(x4, y4)