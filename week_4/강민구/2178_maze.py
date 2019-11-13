import copy
from collections import deque
import sys

x, y = map(int, sys.stdin.readline().split()) # 미로의 크기 결정
maze = [[0]*y for _ in range(x)] # X x Y  행렬의 미로
visit = copy.deepcopy(maze) # 미로를 방문했다는 표시를 남기기 위한 maze와 똑같은 행렬
for i in range(x) :
    temp = sys.stdin.readline() # 한 줄씩 1과0을 입력
    for j in range(y) :
        maze[i][j] = int(temp[j]) # 최종적인 미로 완성


#동서남북을 표현한 변수 선언
direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]

#큐 생성
que = deque()
que.append((0,0)) # 시작은 0,0이므로 큐에 넣고 시작
visit[0][0] = 1 #시작점을 방문 시키고 시작
# BFS 시작
while que :

    a,b = que.popleft()
    # que에서 나온 값이 도착해야할 곳이라면 종료
    if a == x-1 and b == y-1 :
        print(visit[a][b])
        break
    #동서남북 탐색 시작
    for n in range(4) :
        ax = a + direction_x[n]
        ay = b + direction_y[n]
        if ax >= 0 and ax < x and ay >= 0 and ay < y :
            if visit[ax][ay] == 0 and maze[ax][ay] == 1 :
                visit[ax][ay] = visit[a][b] + 1
                que.append((ax,ay))


