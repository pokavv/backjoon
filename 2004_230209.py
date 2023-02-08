import sys
input = sys.stdin.readline

a, b = map(int, input().split())

# nCr(조합) = n! / (n-r)! * r!
# factorial은 시간초과 발생
# 끝 자릿수 0은 10의 배수 (2 * 5)

def cnt_num(num, val):
    cnt = 0
    while num:
        num //= val
        cnt += num
    return cnt

five_cnt = cnt_num(a, 5) - cnt_num(b, 5) - cnt_num(a - b, 5)
two_cnt = cnt_num(a, 2) - cnt_num(b, 2) - cnt_num(a - b, 2)

# 2와 5의 짝이 맞아야 10이 되므로 five_cnt와 two_cnt 중 더 작은게 10의 개수
res = min(five_cnt, two_cnt)
print(res)