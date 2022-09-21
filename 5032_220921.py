emptyb, getb, needb = map(int, input().split())

bottle_sum = emptyb + getb
n = 0
while bottle_sum >= needb:
    n += bottle_sum // needb
    bottle_sum = (bottle_sum // needb) + (bottle_sum % needb)

print(n)