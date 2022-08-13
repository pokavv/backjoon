test_case = int(input())

for i in range(test_case):
    Yscore = 0
    Kscore = 0
    for j in range(9):
        yonsei, korea = map(int, input().split(" "))
        Yscore += yonsei
        Kscore += korea
    
    if Yscore > Kscore:
        print("Yonsei")
    elif Yscore < Kscore:
        print("Korea")
    else:
        print("Draw")