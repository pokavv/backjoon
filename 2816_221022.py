channel_num = int(input())
channel = []

for i in range(channel_num):
    channel_name = input()
    if channel_name == 'KBS1':
        arrow1 = i
    elif channel_name == 'KBS2':
        arrow2 = i
    channel.append(channel_name)

res = ''
res += '1' * arrow1
res += '4' * arrow1

if arrow1 > arrow2:
    arrow2 += 1

res += '1' * arrow2
res += '4' * (arrow2 - 1)
print(res)