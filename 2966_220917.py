import sys
num = int(sys.stdin.readline())
ans = sys.stdin.readline().rstrip()

s_pick = ['A', 'B', 'C']
c_pick = ['B', 'A', 'B', 'C']
h_pick = ['C', 'C', 'A', 'A', 'B', 'B']

s_res = 0
c_res = 0
h_res = 0

for i in range(num):
    if ans[i] == s_pick[i % 3]:
        s_res += 1
    
    if ans[i] == c_pick[i % 4]:
        c_res += 1
        
    if ans[i] == h_pick[i % 6]:
        h_res += 1

win_res = max(s_res, c_res, h_res)
print(win_res)

if win_res == s_res:
    print('Adrian')
if win_res == c_res:
    print('Bruno')
if win_res == h_res:
    print('Goran')