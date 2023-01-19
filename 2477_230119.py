import sys
input = sys.stdin.readline

kmelon = int(input())
field_info = [list(map(int, input().split())) for _ in range(6)]

width = 0
height = 0
widx = 0
hidx = 0

# east 1, west 2, south 3, north 4
for i in range(len(field_info)):
    if field_info[i][0] == 1 or field_info[i][0] == 2:
        if width < field_info[i][1]:
            width = field_info[i][1]
            widx = i
    elif field_info[i][0] == 3 or field_info[i][0] == 4:
        if height < field_info[i][1]:
            height = field_info[i][1]
            hidx = i

subwidth = abs(field_info[(widx - 1) % 6][1] - field_info[(widx + 1) % 6][1])
subheight = abs(field_info[(hidx - 1) % 6][1] - field_info[(hidx + 1) % 6][1])

print(((width * height) - (subwidth * subheight)) * kmelon)