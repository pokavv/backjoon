chess_piece = [1, 1, 2, 2, 2, 8]
input_list = list(map(int, input().split()))

for i in range(6):
    print(chess_piece[i] - input_list[i], end=' ')