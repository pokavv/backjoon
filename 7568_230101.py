import sys
input = sys.stdin.readline

n = int(input())
data = []
ranking = []

for _ in range(n):
    height, weight = map(int, input().split())
    data.append((height, weight))

for i in range(n):
    rank = 0
    
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            rank += 1
    
    ranking.append(rank + 1)

for rank in ranking:
    print(rank, end=' ')