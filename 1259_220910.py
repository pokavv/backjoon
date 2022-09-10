while True:
    isPal = input()
    
    if isPal == '0':
        break
    elif isPal == isPal[::-1]:
        print('yes')
    else:
        print('no')