import sys
input = sys.stdin.readline

N, M = map(int, input().split())
string_set = set()
# set는 hash table 구조를 사용하기 때문에 시간복잡도에서 list보다 유리함

for _ in range(N):
    string_set.add(input())

cnt = 0
for _ in range(M):
    if input() in string_set:
        cnt += 1

print(cnt)