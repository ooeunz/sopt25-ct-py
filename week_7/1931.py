count = int(input())
conference = []
result = 0
for _ in range(count):
    start,end= input().split()
    start = int(start)
    end = int(end)
    conference.append((start,end))
conference = sorted(conference,key=lambda conference: conference[0])
conference = sorted(conference,key=lambda conference: conference[1])
start = -1
for time in conference:
    if(time[0]>=start):
        result = result + 1
        start = time[1]
print(result)