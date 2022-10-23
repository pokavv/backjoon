import sys

result = 0
cards = [list(sys.stdin.readline().strip()) for _ in range(5)]
colors = [x[0] for x in cards]
numbers = [int(x[2]) for x in cards]

hash_color = {}
hash_number = {}

for c in colors:
    if c in hash_color:
        hash_color[c] += 1
    else:
        hash_color[c] = 1

for n in numbers:
    if n in hash_number:
        hash_number[n] += 1
    else:
        hash_number[n] = 1

numbers.sort()

color = []
number = []

def color_match(n):
    global color
    
    for k, v in hash_color.items():
        if v == n:
            color.append(k)
            return True
    return False

def number_match(n):
    global number

    result = False

    for k, v in hash_number.items():
        if v == n:
            number.append(k)
            result = True

    return result

def is_seq():
    global numbers

    prev = None

    for k in numbers:
        if prev != None:
            if (prev + 1) != k:
                return False
        prev = int(k)
    return True

if color_match(5) and is_seq():
    result += (900 + numbers[4])
elif number_match(4):
    result += (800 + number[0])
elif number_match(3) and number_match(2):
    result += (700 + (10 * number[0]) + number[1])
elif color_match(5):
    result += (600 + numbers[4])
elif is_seq():
    result += (500 + numbers[4])
elif number_match(3):
    result += (400 + number[0])
elif number_match(2) and (len(number) == 2):
    number.sort()
    result += (300 + number[0] + (number[1] * 10))
elif number_match(2):
    result += (200 + number[0])
else:
    result += (100 + numbers[4])
print(result)

# 출처: https://futuregate.tistory.com/24 [미래문 :: 코딩과 일상:티스토리]