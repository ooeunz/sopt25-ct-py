# 1931 - 회의실배

# 가장 많은 회의의 수를 알기 위해서는 빨리 끝나는 회의 순서대로 정렬해야함
# 빨리 끝나는 것 중 빨리 시작하는 순서대로

import sys

n = int(input())
meeting = []
for _ in range(n):
    meeting.append(list(map(int, sys.stdin.readline().split())))

meeting = sorted(meeting, key=lambda x: [x[1], x[0]])

result = 0
start = 0
for meet in meeting:
    if meet[0] >= start:
        start = meet[1]
        result += 1

print(result)
