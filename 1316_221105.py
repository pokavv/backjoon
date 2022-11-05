import sys
input = sys.stdin.readline
group_word = 0

for _ in range(int(input())):
    cnt = 0
    word = input()
    
    for i in range(len(word) - 1):
        if word[i] != word[i+1]:
            new_word = word[i+1:]
            if new_word.count(word[i]) > 0:
                cnt += 1
    
    if cnt == 0:
        group_word += 1

print(group_word)