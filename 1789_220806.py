max_num = int(input())
num = 1

# 1부터 n까지의 합 공식: n(n+1)/2
while num * (num + 1) / 2 <= max_num:
    num += 1

# 최대값보다 커지므로 num에서 1을 뺌
print(num - 1)