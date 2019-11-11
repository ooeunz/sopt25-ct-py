from collections import deque
import sys


# initialization
AROUND = ((-1, 0), (0, 1), (1, 0), (0, -1))

# create map
row, col, size_y, size_x, K = map(int, sys.stdin.readline().split())

maps = [[1] * col for _ in range(row)]
visited = set()

# create obstacle
for _ in range(K):
    y, x = map(lambda x: int(x)-1, sys.stdin.readline().split())
    maps[y][x] = 0

# start, end points
start_y, start_x = map(lambda x: int(x)-1, sys.stdin.readline().split())
end_y, end_x = map(lambda x: int(x)-1, sys.stdin.readline().split())

def collections(next_y, next_x):
    # check bounds and obstacle
    for y in range(size_y):
        for x in range(size_x):
            unit_y = next_y + y
            unit_x = next_x + x
            if not (0 <= unit_y < row and 0 <= unit_x < col) or not maps[unit_y][unit_x]:
                return True
    return False

def game():
    queue = deque([[start_y, start_x, 0]])
    visited.add((start_y, start_x))
    while queue:
        y, x, dist = queue.popleft()

        for dy, dx in AROUND:
            next_y = y + dy
            next_x = x + dx

            if (next_y, next_x) in visited:
                continue

            if next_y == end_y and next_x == end_x:
                return dist + 1

            if not collections(next_y, next_x):
                queue.append([next_y, next_x, dist+1])
                visited.add((next_y, next_x))
    return -1

if __name__ == "__main__":
    print(game())
