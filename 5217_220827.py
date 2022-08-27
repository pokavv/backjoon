for i in range(int(input())):
    num = int(input())
    print(f"Pairs for {num}:", end=' ')
    for j in range(1, num // 2 + 1):
        if j != num - j:
            if j != 1:
                print(',', end=' ')
            print(j, num - j, end='')
    print()