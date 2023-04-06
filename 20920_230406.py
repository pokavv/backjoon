import sys
input = sys.stdin.readline
word_num, cut_length = map(int, input().split())
voca_dict = {}

for _ in range(word_num):
    word = input().rstrip()
    
    if len(word) < cut_length:
        continue
    else:
        if word in voca_dict:
            voca_dict[word] += 1
        else:
            voca_dict[word] = 1

voca_dict = sorted(voca_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
# -x[1] = 자주 나오는 단어 앞에 배치
# -len(x[0]) = 단어 길이 길수록 앞에 배치
# x[0] = 단어 사전 순 정렬

for i in voca_dict:
    print(i[0])