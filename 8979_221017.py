import sys
input = sys.stdin.readline

country_num, key_country = map(int, input().split())
ranking = []

for i in range(country_num):
    ranking.append(list(map(int, input().split())))

ranking.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for i in range(country_num):
    if ranking[i][0] == key_country:
        index = i

for i in range(country_num):
    if ranking[index][1:] == ranking[i][1:]:
        print(i + 1)
        break