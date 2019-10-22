from operator import itemgetter, attrgetter

T = int(input())
location = []

for _ in range(T) :
    x, y = map(int, input().split())
    location.append([x,y])

location.sort(key = itemgetter(0,1))

for (a,b) in location :
    print("{0} {1}".format(a,b))

