import sys
input = sys.stdin.readline
pokemon_num, problem_num = map(int, input().split())
encyclopedia = {}

for i in range(1, pokemon_num + 1):
    pokemon = input().rstrip()
    encyclopedia[i] = pokemon
    encyclopedia[pokemon] = i

for i in range(problem_num):
    problem = input().rstrip()
    if problem.isdigit():
        print(encyclopedia[int(problem)])
    else:
        print(encyclopedia[problem])