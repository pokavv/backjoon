num = list(map(int, input().split()))
A = sorted(num)

if num == A:
    print('Good')
else:
    print('Bad')