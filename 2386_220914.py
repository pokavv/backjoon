while True:
    alp_str = input().lower()
    if alp_str == '#':
        break
    
    alp = alp_str[0]
    tstr = alp_str[2:]
    res = tstr.count(alp)
    print(alp, res)