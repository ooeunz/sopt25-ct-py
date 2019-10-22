from operator import itemgetter, attrgetter

T = int(input())
location = []

for _ in range(T) :
    a = list(map(int, input().split()))
    location.append(a)

location.sort(key = itemgetter(1,0))

for (a,b) in location :
    print("{0} {1}".format(a,b))

