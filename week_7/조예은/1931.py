# 그리디 - 회의실 배정 
# 회의가 빨리 끝나야 많은 회의를 진행할 수 있으므로 끝나는 시간 오름차순으로 정렬
# 만약 같은 시간에 끝난다면 늦게 시작하는 순서로 정렬
# 현재 회의 끝나는 시간과 다음 회의의 시작하는 시간 비교하여 count

import sys

schedule = []
N = int(input())
for i in range(N):
    schedule.append(tuple(map(int, sys.stdin.readline().split())))
sortList = sorted(schedule, key= lambda x: (x[1], x[0]))

end = sortList[0][1]
answer = 1
for i in range(N):
    if end <= sortList[i][0] and i > 0:
        answer += 1
        end = sortList[i][1]
print(answer)