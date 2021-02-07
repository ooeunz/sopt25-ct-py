import heapq
N = int(input())
quest = [] # (데드라인, 컵라면 갯수)로 구성된 리스트
result = [] # minheap으로 만들 리스트
for _ in range(N) :
    quest.append(tuple(map(int,input().split())))
quest = sorted(quest, key = lambda x:(x[0],-x[1])) # 데드라인으로 오름차순 라면갯수로 내림차순 설정
deadline = 1
for dead,noodle in quest :
    if deadline <= dead :
        deadline += 1
        heapq.heappush(result,noodle)
    elif result and result[0] < noodle :
        heapq.heappop(result)
        heapq.heappush(result,noodle)
print(sum(result))