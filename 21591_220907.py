l_width, l_height, s_width, s_height = map(int, input().split())

if l_width >= (s_width + 2) and l_height >= (s_height + 2):
    print(1)
else:
    print(0)