people = int(input())
time = input().split(" ")
for i in range(0, len(time)):
    time[i] = int(time[i])
time.sort()
result = 0
i=0
while people != 0:
    result += time[i]

    if i < len(time)-1:
        time[i+1] += time[i]
    people-=1
    i+=1
print(result)
