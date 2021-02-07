# 그리디 알고리즘 - 기다리는 시간 최소 구하기
# 시간 오름차순으로 정렬해주고 짧은 순서대로 계속 더해주기

import sys
answer = 0
num = int(input())
time = list(map(int, sys.stdin.readline().split()))
time.sort()
for i in range(len(time)):
    answer += time[i] * (num-i)
print(answer)