# 지나가야하는 방의 개수 +1 : +6
num = int(input())
fold = 1
cnt = 1

while num > fold:
    fold += 6 * cnt # 6의 배수로 증가
    cnt += 1

print(cnt)