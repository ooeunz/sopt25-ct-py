# N = 학생 수 , M = 단방향 도로 수 , X = 파티 장소
import sys
import heapq

def dijk(village,result,X) :
    result[X-1] = 0 #파티 장소는 최단 경로가 0
    que = [] #최소 힙
    heapq.heappush(que,(result[X-1], result.index(result[X-1]))) #(최단경로,해당 인덱스)

    while que :
        vertex, index = heapq.heappop(que) # vertex = 최단 경로, index = 해당 인덱스
        if result[index] < vertex : # 현재 경로값이 큐값에서 나온 값보다 작으면 패스
            continue
        else :
            for x, y in village[index+1].items() : #x는 현재 정점과 인접한 또 다른 정점 , y는 가중치
                weight = y + vertex
                if result[x-1] >= weight :
                    result[x-1] = weight
                    heapq.heappush(que,(result[x-1], x-1)) #(경로가중치, 인덱스)

input = sys.stdin.readline
INF = sys.maxsize
N, M, X = map(int,input().split()) #학생 수, 도로 수, 파티장소 입력
village = {} # 그래프를 표현한 딕셔너리
rev_village={} # 역방향 그래프를 표현한 딕셔너리
result = [INF for _ in range(N)] #정방향 그래프 다익스트라
rev_result=[INF for _ in range(N)] #역방향 그래프 다익스트라
for i in range(1,N+1) :
    village[i]={}
    rev_village[i]={}
for _ in range(M) :
    u,v,w = map(int,input().split()) # u = 시작점 v = 끝점 w = 가중치
    village[u][v] = w
    rev_village[v][u] = w

dijk(village,result,X) # 파티장소 -> 각 마을 최소 경로 탐색
dijk(rev_village,rev_result,X) # 역방향 그래프를 이용한  각 마을 -> 파티장소 최소 경로 탐색

for i in range(len(result)) :
    result[i] += rev_result[i]
print(max(result))