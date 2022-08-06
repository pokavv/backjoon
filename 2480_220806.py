adice, bdice, cdice = map(int, input().split())
a, b, c = adice, bdice, cdice
dice_list = [adice, bdice, cdice]

if a == b == c:
    print(10000 + (a * 1000))
elif a == b:
    print(1000 + (a * 100))
elif a == c:
    print(1000 + (a * 100))
elif b == c:
    print(1000 + (b * 100))
else:
    dice_list.sort
    biggiest_num = dice_list[0]
    print(biggiest_num * 100)