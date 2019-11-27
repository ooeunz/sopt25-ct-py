import sys


scores = [int(sys.stdin.readline()) for _ in range(5)]
scores = [40 if score < 40 else score for idx, score in enumerate(scores) ]

print(sum(scores)//5)