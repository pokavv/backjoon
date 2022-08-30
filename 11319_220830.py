eng_vowel = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

for i in range(int(input())):
    str = input()
    cons = 0
    vowel = 0
    for j in str:
        if j in eng_vowel:
            vowel += 1
        elif j.isalpha():
            cons += 1
    print(cons, vowel)