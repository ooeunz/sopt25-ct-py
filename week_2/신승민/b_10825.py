import sys

n = int(sys.stdin.readline())
score_list = []

for _ in range(n):
    score_list.append(sys.stdin.readline().strip().split())

score_list.sort(key= lambda score: score[0]) # sorted by name
score_list.sort(key= lambda score: int(score[3]), reverse=True) # sorted by math
score_list.sort(key= lambda score: int(score[2])) # sorted by eng
score_list.sort(key= lambda score: int(score[1]), reverse=True) # sorted by kor

print('\n'.join(map(lambda score: score[0], score_list)))
    