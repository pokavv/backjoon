price, snack, money = map(int, input().split())
how_much = price * snack - money

if how_much > 0:
    print(how_much)
else:
    print(0)