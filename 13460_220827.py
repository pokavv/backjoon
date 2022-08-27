from collections import deque
import sys
input = sys.stdin.readline
row, column = map(int, input().split())
board =[]

# Check up, down, left, right
qx = [-1, 1, 0, 0]
qy = [0, 0, -1, 1]

for i in range(row):
    board.append(list(input()))
    for j in range(column):
        if board[i][j] == 'R':  # Red marble's position
            redx, redy = i, j
        elif board[i][j] == 'B':    # Blue marble's position
            bluex, bluey = i, j

def bfs(redx, redy, bluex, bluey):
    dq = deque()
    dq.append((redx, redy, bluex, bluey))
    visited_list = [] # List for determining whether to visit
    visited_list.append((redx, redy, bluex, bluey))
    count = 0

    while dq:
        for i in range(len(dq)):
            redx, redy, bluex, bluey = dq.popleft()
            if count > 10: # Print -1 when the number of moves exceeds 10
                print(-1)
                return
            if board[redx][redy] == 'O': # If the position of the red marble is O, output count
                print(count)
                return
            for i in range(4): # 4-way check
                qredx, qredy = redx, redy
                while True: # Repeat until '#' or 'O'
                    qredx += qx[i]
                    qredy += qy[i]
                    if board[qredx][qredy] == '#': # If '#', move backward 1
                        qredx -= qx[i]
                        qredy -= qy[i]
                        break
                    if board[qredx][qredy] == 'O':
                        break
                qbluex, qbluey = bluex, bluey
                while True: # Repeat until '#' or 'O'
                    qbluex += qx[i]
                    qbluey += qy[i]
                    if board[qbluex][qbluey] == '#': # If '#', move backward 1
                        qbluex -= qx[i]
                        qbluey -= qy[i]
                        break
                    if board[qbluex][qbluey] == 'O':
                        break
                # Blue marbles must not enter the 'O' first or at the same time
                if board[qbluex][qbluey] == 'O':
                    continue
                if qredx == qbluex and qredy == qbluey: # If the two marbles are in the same position:
                # The marble that moved more moves later because the marble that moved more moves backward one space.
                    if abs(qredx - redx) + abs(qredy - redy) > abs(qbluex - bluex) + abs(qbluey - bluey):
                        qredx -= qx[i]
                        qredy -= qy[i]
                    else:
                        qbluex -= qx[i]
                        qbluey -= qy[i]
                # If a location has never been visited, it is added to the queue and processed.
                if (qredx, qredy, qbluex, qbluey) not in visited_list:
                    dq.append((qredx, qredy, qbluex, qbluey))
                    visited_list.append((qredx, qredy, qbluex, qbluey))
        count += 1
    print(-1) # not been exceed 10, but cannot be entered within 10
bfs(redx, redy, bluex, bluey)