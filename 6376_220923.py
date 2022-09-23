import math

res = 0

print('n e')
print('- -----------')
for i in range(10):
    res += 1 / math.factorial(i)
    
    if res > 2.5:
        print(f'{i} %.9f' % res)
    elif res == 1 or res == 2:
        print(f'{i} {int(res)}')
    elif res == 2.5:
        print(f'{i} %.1f' % res)