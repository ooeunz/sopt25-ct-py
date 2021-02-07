# 사탕 개수를 최대로 하는 미로에서 이동하기 문제
# 당장의 오른쪽, 아래, 대각선의 사탕개수만 고려하면 안 됨
# 역으로 해당 구간이 가질 수 있는 최대값을 구해서 마지맘 NxM 자리에 저장 후 출력

import sys

n, m = map(int, sys.stdin.readline().split())
maze = [[0]*(m+1)]
for _ in range(n):
    maze.append([0]+ list(map(int, sys.stdin.readline().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        maze[i][j] += max(maze[i-1][j], maze[i][j-1], maze[i-1][j-1])
print(maze[i][j])