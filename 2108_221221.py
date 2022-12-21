import sys
from collections import Counter # 최빈값 구하기 위해 collections 모듈의 Counter class 이용
input = sys.stdin.readline
numbers = int(input())

arr = []
for _ in range(numbers):
    arr.append(int(input()))
arr.sort()

# 산술평균
print(round(sum(arr)/numbers))

# 중앙값
print(arr[int((numbers - 1)/2)])

# 최빈값
def mostVal(arr):
    most_value = Counter(arr).most_common()
    if len(most_value) > 1:
        if most_value[0][1] == most_value[1][1]:
            print(most_value[1][0])
        else:
            print(most_value[0][0])
    else:
        print(most_value[0][0])

mostVal(arr)

# 범위
print(arr[-1] - arr[0])