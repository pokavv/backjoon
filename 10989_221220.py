import sys
input = sys.stdin.readline

board = [0] * 10001

for _ in range(int(input())):
    board[int(input())] += 1

for i in range(10001):
    if board[i]:
        for _ in range(board[i]):
            print(i)

#######################################
# 메모리 초과
'''
num_list = []

for _ in range(int(input())):
    num_list.append(int(input()))

num_list.sort()

for i in num_list:
    print(i)
'''