h, m = map(int, input().split())

h -= 1
m += 60
m -= 45
if m >= 60:
    m -= 60
    h += 1
if h < 0:
    h += 24
print(h, m)