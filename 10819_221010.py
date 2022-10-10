import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
permutations_arr = list(permutations(arr, n))
res  = 0

# permutations(): 순서를 고려해 나열한 경우의 수 nPr <-> combination()
print(permutations_arr)

for i in range(len(permutations_arr)):
    tmp = 0
    for j in range(0, n - 1):
        tmp += abs(permutations_arr[i][j] - permutations_arr[i][j + 1]) # abs(): 절대값 함수
    if tmp > res:
        res = tmp

print(res)