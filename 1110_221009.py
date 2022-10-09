'''
1. 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리수로 만들고 각 자리의 숫자를 더한다.
2. 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어붙이면 새로운 수를 만들 수 있음
'''

num = int(input())
first_num = num
cnt = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c
    
    cnt += 1
    if(num == first_num):
        break

print(cnt)