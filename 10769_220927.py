char = input()
joy = char.count(':-)')
sor = char.count(':-(')

if joy == 0 and sor == 0:
    print('none')
elif joy > sor:
    print('happy')
elif joy == sor:
    print('unsure')
elif joy < sor:
    print('sad')