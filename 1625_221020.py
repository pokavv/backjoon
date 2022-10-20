import sys
input = sys.stdin.readline

room_size = int(input())
room = []
for _ in range(room_size):
    room.append(list(input().strip()))

row = 0
column = 0
for i in range(room_size):
    cnt = 0
    for j in range(room_size):
        if room[i][j] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            row += 1

for i in range(room_size):
    cnt = 0
    for j in range(room_size):
        if room[j][i] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            column += 1

print(row, column)