while True:
    st = input()
    if st == '#':
        break
    
    cnt = 0
    
    for i in st:
        if i in 'aeiouAEIOU':
            cnt += 1
    print(cnt)