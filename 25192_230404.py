import sys
input = sys.stdin.readline

nickname = set()
gomgom = 0

for _ in range(int(input())):
    log = input().rstrip()
    
    if log == 'ENTER':
        nickname.clear()
    
    if log not in nickname and log != 'ENTER':
        nickname.add(log)
        gomgom += 1

# print(nickname)
print(gomgom)