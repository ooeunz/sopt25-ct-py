a,b = map(int,input().split()) # 행렬 크기 지정
candy_map = [[int(n) for n in input().split()] for _ in range(a)] # 캔디맵 생성
dp_map = [[0 for _ in range(b)] for _ in range(a)] # 각 인덱스에 최댓값을 넣어놓는 곳

for x in range(a) :
    for y in range(b):
        dp_map[x][y] = max(dp_map[x-1][y],dp_map[x][y-1]) #이전에 있던 좌표 값에서 큰 값을 가져옴
        dp_map[x][y] += candy_map[x][y] # 현재 위치와 동일한 위치의 캔디값을 더해준다.

print(dp_map[a-1][b-1])