import sys
from collections import deque
#큐를 이용한 BFS 탐색
def BFS(graph,start) :

    for i in graph :
        graph[i].sort()

    visit = []
    que = deque()
    que.append(start)

    while que :
        vertex = que.popleft()
        if vertex not in visit :
            visit.append(vertex)
            que.extend(graph[vertex]) #리스트라서 extend를 이용해 요소만 집어 넣는다

    print(" ".join(map(str,visit)))


#스택을 이용한 DFS 탐색
def DFS(graph,start) :

    for i in graph :
        graph[i].sort(reverse = True)

    visit = []
    stack = []
    stack.append(start)

    while stack :
        vertex = stack.pop()
        if vertex not in visit :
            visit.append(vertex)
            stack.extend(graph[vertex])

    print(" ".join(map(str,visit)))


if __name__ == "__main__" :
    x, y, start = map(int, sys.stdin.readline().split()) #정점의 개수, 간선의 개수, 시작 정점을 받는다
    graph = {} # 딕셔너리로 표시된 그래프
    # 정점들 추가
    for n in range(x) :
        graph[n+1] = []

    #간선 추가
    for _ in range(y) :
        a , b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)



    DFS(graph, start)
    BFS(graph, start)

