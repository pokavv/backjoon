import sys
input = sys.stdin.readline

string = input().rstrip()
arr = [[0] * 26 for _ in range(len(string) + 1)]

q = int(input())
res = []

for i in range(1, len(string) + 1):
    for j in range(26):
        if ord(string[i - 1]) - 97 == j:
            arr[i][j] = arr[i - 1][j] + 1
        else:
            arr[i][j] = arr[i - 1][j]

for _ in range(q):
    a, l, r = input().split()
    a, l, r = ord(a) - 97, int(l), int(r)
    
    print(arr[r + 1][a] - arr[l][a])