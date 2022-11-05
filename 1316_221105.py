import sys
input = sys.stdin.readline
cnt = int(input())

for _ in range(cnt):
    word = input()
    for i in range(0, len(word) - 1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            cnt -= 1
            break

print(cnt)