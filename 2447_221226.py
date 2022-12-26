# n ** i 배열은 가운데칸을 제외하고 n ** (i - 1)의 배열 각 칸마다 그림

def drawStars(n):
    board = [] # 배열 board 생성
    for i in range(len(n) * 3): # line * 3
        if i // len(n) == 1: # 몫이 1일 때
            board.append(n[i % len(n)] + ' ' * len(n) + n[i % len(n)]) # 배열 공백
        else:
            board.append(n[i % len(n)] * 3)
    return board

n = int(input()) # 별 배열 사이즈 설정: 크기 n*n
star_shape = ['***', '* *', '***'] # n = 3일 때 별모양 list
cnt = 0

while n != 3: # n이 3이 아니면
    n //= 3 # n = n // 3
    cnt += 1 # + 1 count

for _ in range(cnt): # cnt 반복
    star_shape = drawStars(star_shape)

for line in star_shape: # board 출력
    print(line)