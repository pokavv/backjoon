import sys
input = sys.stdin.readline

def bridge_construction(a, b):
    tmp = [[1] * 31 for _ in range(31)]
    
    for i in range(31):
        tmp[1][i] = i
    
    for i in range(2, 31):
        for j in range(i + 1, 31):
            tmp[i][j] = tmp[i][j - 1] + tmp[i - 1][j - 1]
    
    print(tmp[a][b])

for _ in range(int(input())):
    west_site, east_site = map(int, input().split())
    bridge_construction(west_site, east_site)