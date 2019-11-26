N = int(input())
people = list(map(int,input().split()))
people.sort()
answer = 0
time = 0
for person in people :
    time += person
    answer += time
print(answer)