rect = input().split()
rect = list(map(int, rect))
rect.sort()
print(rect[0]*rect[2])