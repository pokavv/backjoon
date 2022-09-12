octo_dic = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}

while 1:
    octo_num = input()
    if octo_num == '#':
        break
    trans = 0
    
    for i in range(len(octo_num)):
        trans += octo_dic[octo_num[i]] * (8 ** (len(octo_num) - i - 1))
    print(trans)