import sys
from collections import deque

# N = node의 개수, M = 간선의 개수, V = start node
N, M, V = map(int, sys.stdin.readline().split())
matrix = [[0] * (N + 1) for _ in range(N+1)]

for _ in range(M):
    x, y = map(int,  sys.stdin.readline().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

def dfs(current_node, row, visited):
    visited.append(current_node)
    for search_node in range(len(row[current_node])):
        if row[current_node][search_node] and not search_node in visited:
            visited = dfs(search_node, row, visited)
    return visited

def bfs(start):
    queue = deque([start])
    visited = [start]
    while queue:
        current_node = queue.popleft()
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and not search_node in visited:
                queue.append(search_node)
                visited.append(search_node)
    return visited

print(*dfs(V, matrix, []))
print(*bfs(V))