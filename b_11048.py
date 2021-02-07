import queue
import math

n, m = tuple(map(int,input().split()))

board =[list(map(int, input().split())) for _ in range(n)]
ret = [[0]*m for _ in range(n)]

def in_board(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

d = [(-1,0), (0,-1)]

ret[0][0] = board[0][0]
for x in range(1, n):
    ret[x][0] = board[x][0] + ret[x-1][0]

for y in range(1, m):
    ret[0][y] = board[0][y] + ret[0][y-1]

for x in range(1, n):
    for y in range(1, m):
        ret[x][y] = board[x][y] + max([ret[x+dx][y+dy] for dx, dy in d if in_board(x+dx, y+dy)])

print(ret[n-1][m-1])