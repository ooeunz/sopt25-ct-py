from operator import itemgetter, attrgetter
N = int(input())
a = []
meeting=[]
for _ in range(N):
    a.append(tuple(map(int,input().split())))
a = sorted(a, key=itemgetter(1,0))
for meet in a :
    if not meeting :
        meeting.append(meet)
    else :
        if meet[0] >= meeting[-1][1] :
            meeting.append(meet)

print(len(meeting))