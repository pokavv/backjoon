import sys
input = sys.stdin.readline
word = []

for _ in range(int(input())):
    word.append(input().strip())

word = list(set(word)) # 중복 제거
word.sort(key=lambda x: (len(x), x))
res = '\n'.join(word)
print(res)