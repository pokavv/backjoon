word = input().upper()
li = list(set(word))

cnt = []
for i in li:
    cnt.append(word.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(li[(cnt.index(max(cnt)))])