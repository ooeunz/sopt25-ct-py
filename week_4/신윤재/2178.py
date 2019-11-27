import sys
from collections import deque

AROUND = ((-1, 0), (0, 1), (1, 0), (0, -1))

row, col = map(int, sys.stdin.readline().split())
maps = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(row)]

def solution(start):
    queue = deque([start])
    check = [[False]*col for _ in range(row)]
    dist = [[0]*col for _ in range(row)]
    dist[0][0] = 1
    
    while queue:
        y, x = queue.popleft()
        for dy, dx in AROUND:
            next_x = x + dx
            next_y = y + dy
            
            if 0 <= next_y < row and 0 <= next_x < col: # check bounds
                if maps[next_y][next_x] and not check[next_y][next_x]:
                    queue.append((next_y, next_x))
                    dist[next_y][next_x] = dist[y][x] + 1
                    check[next_y][next_x] = True

    return dist[row-1][col-1]

print(solution((0, 0)))