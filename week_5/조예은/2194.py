import sys

map_n, map_m, unit_a, unit_b, obstacle = map(int, sys.stdin.readline().split())
map = [[0] * map_m for _ in range(map_n)]

for _ in range(obstacle):
    ob_x, ob_y = map(int, sys.stdin.readline().split())
    map[ob_x][ob_y] = 1

start_x, start_y = map(int, sys.stdin.readline().split())
end_x, end_y = map(int, sys.stdin.readline().split())

