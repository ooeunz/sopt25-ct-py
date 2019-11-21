'''
import sys

map_n, map_m, unit_a, unit_b, obstacle = map(int, sys.stdin.readline().split())
map = [[0] * map_m for _ in range(map_n)]

for _ in range(obstacle):
    ob_x, ob_y = map(int, sys.stdin.readline().split())
    map[ob_x][ob_y] = 1

start_x, start_y = map(int, sys.stdin.readline().split())
end_x, end_y = map(int, sys.stdin.readline().split())



import sys
import math

n, m, a, b, k = (map(int, sys.stdin.readline().split()))
d = [(-1,0), (1,0), (0,-1), (0,1)]
break_points = set()
visited = []
cached = {}

def in_board(p):
    x, y = p
    return 1 <= x and x <= n - a + 1 and 1 <= y and y <= m - b + 1

# s, e is a tuple
def find_min_route(s, e, history = [], depth = 0):
    if s in cached:
        # print(f'hit cache {cached[s]}')
        return cached[s]

    if s in visited or not in_board(s) or s in break_points:
        return math.inf

    history.append(s)
    depth += 1
    if s == e:
        print('history = {history}')
        print('depth = {depth}')
        return 0
    else:
        visited.append(s)
        cached[s] = min([find_min_route((s[0] +dx, s[1] + dy), e, [], depth) for dx, dy in d]) + 1
        return cached[s]


for _ in range(k):
    bx, by = map(int, sys.stdin.readline().split())
    break_points.update([(bx-dx, by-dy) for dx in range(0, a) for dy in range(0, b)])

print(break_points)

fs = tuple(map(int, sys.stdin.readline().split()))
e = tuple(map(int, sys.stdin.readline().split()))

min_route = find_min_route(fs, e)
if min_route == math.inf:
    print("-1")
else:
    print(str(min_route))
    '''