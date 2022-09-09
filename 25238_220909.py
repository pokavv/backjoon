mob_defense, ignore_defense = map(int, input().split())

if mob_defense - (ignore_defense/100 * mob_defense) >= 100.0:
    print(0)
else:
    print(1)