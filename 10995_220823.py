star = int(input())

if star == 1:
    print('*')
else:
    for i in range(star):
        if i % 2 == 0:
            print('* ' * star)
        else:
            print(' *' * star)