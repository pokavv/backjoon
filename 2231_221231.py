N = int(input())

# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 
# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다.

for i in range(1, N + 1):
    sum_decomposition = i + sum(map(int, str(i)))
    if sum_decomposition == N:
        print(i)
        break
    if i == N:
        print(0)