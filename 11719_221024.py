while True:
    try:
        print(input())
    except EOFError: # 더 이상 입력할 것이 없음
        break