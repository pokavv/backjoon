def recursive(arr, start, now_len):
    tmp = now_len // 3
    
    if tmp == 0:
        return
    
    for i in range(start + tmp, start + (tmp * 2)):
        arr[i] = ' '
    
    recursive(arr, start, tmp)
    recursive(arr, start + (tmp * 2), tmp)

while True:
    try:
        res = ''
        n = input()
        if n == '':
            break
        else:
            n = int(n)
            arr = ['-' for i in range(pow(3, n))] # pow : 제곱함수. pow(x, y) x의 y승
            recursive(arr, 0, pow(3, n))
            
            for i in arr:
                res += i
            print(res)
    except EOFError: # EOFError 예외처리로 반복문 종료시킴
        break

##############################################################

import sys
input = sys.stdin.readline

def recursive(n, i, j):  # 몇 번 더 볼지, 시작점, 끝점
    if n == 0:
        return
    # 3등분
    cnt = (j - i + 1) // 3  # 각각 몇 개씩인지
    # 왼쪽
    recursive(n - 1, i, i + cnt - 1)
    # 가운데 -> 공백으로 바꾸기
    for k in range(i + cnt, i + (cnt * 2)):
        answer[k] = ' '
    # 오른쪽
    recursive(n - 1, i + (cnt * 2), i + (cnt * 3) - 1)

while True:
    try:
        n = int(input())
        answer = ['-'] * (3 ** n)
        recursive(n, 0, (3 ** n) - 1)
        print(''.join(answer))
    except:
        break

##############################################################

import sys

for i in sys.stdin:
    tmp = '-'
    for j in range(int(i)):
        tmp = tmp + ' ' + len(tmp) + tmp
    print(tmp)