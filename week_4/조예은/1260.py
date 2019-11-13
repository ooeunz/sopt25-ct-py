# DFS, BFS
from collections import deque

def DFS():
    return None

def BFS():
    q = deque()
    #current()

if __name__ == "__main__":
    edgeList = list()
    vertexList = list()
    adjacList = list()

    vertexs, edges, start = map(int, input().split(' '))

    for vertex in range(vertexs):
        vertexList.append(str(vertex+1))
    for _ in range(edges):
        edgeList.append(input().split(' '))

    adjacList =  [[] for i in vertexList]
    for edge in edgeList:
        adjacList[edge[0]].append(edge[1])
    print(adjacList)