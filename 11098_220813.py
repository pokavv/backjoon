test_case = int(input())

for i in range(test_case):
    player_info = int(input())
    max_price = 0
    max_name = ""
    for j in range(player_info):
        player_price, player_name = input().split()
        if int(player_price) > max_price:
            max_price = int(player_price)
            max_name = player_name
    
    print(max_name)