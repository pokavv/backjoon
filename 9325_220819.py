for i in range(int(input())):
    car_price = int(input())
    for j in range(int(input())):
        specific_option, so_price = map(int, input().split())
        car_price += specific_option * so_price
    print(car_price)