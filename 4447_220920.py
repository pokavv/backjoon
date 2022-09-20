for i in range(int(input())):
    st = input()
    g_cnt = st.count('g') + st.count('G')
    b_cnt = st.count('b') + st.count('B')
    
    if g_cnt > b_cnt:
        print(f'{st} is GOOD')
    elif g_cnt < b_cnt:
        print(f'{st} is A BADDY')
    else:
        print(f'{st} is NEUTRAL')