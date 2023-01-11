input_string = input()
substring_set = set()

for i in range(len(input_string)):
    for j in range(i, len(input_string)):
        substring_set.add(input_string[i:j+1])

print(len(substring_set))