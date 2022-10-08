while True:
    # try: (예외가 발생할 수도 있는 코드)
    try:
        print(input())
    # except: (예외가 발생했을 경우 실행되는 코드)
    except EOFError: # EOFError: End Of File Error (data가 ㅇ벗어 더이상 값을 읽을 수 없음)
        break