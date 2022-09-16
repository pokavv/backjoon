import sys
cnt = []

for i in range(1, 6):
    name = sys.stdin.readline()
    if 'FBI' in name:
        cnt.append(i)

if len(cnt) > 0:
    print(*cnt)
else:
    print('HE GOT AWAY!')