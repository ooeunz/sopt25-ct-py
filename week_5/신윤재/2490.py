from collections import Counter


rule = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 0: 'E'}
for _ in range(3):
    game = Counter(list(map(int, input().split())))
    print(rule[game[0]])
