import sys

st = sys.stdin.read()
alpha = [0] * 26

for i in st:
    if i.islower():
        alpha[ord(i) - 97] += 1
for i in range(26):
    if alpha[i] == max(alpha):
        print(chr(97 + i), end='')