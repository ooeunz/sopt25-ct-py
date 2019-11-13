import sys

n = int(sys.stdin.readline())
point_list = []

for _ in range(n):
    point_list.append(tuple(int(x.strip()) for x in sys.stdin.readline().split(' ')))

point_list.sort(key= lambda point: point[0]) # sorted by x
point_list.sort(key= lambda point: point[1]) # sorted by y

print('\n'.join(list(map(lambda point: f'{point[0]} {point[1]}', point_list))))