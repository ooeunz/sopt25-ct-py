def solution(people, limit):
    answer = 0
    people.sort()
    start = 0 
    end = len(people)-1
    while(len(people) is not 0):
        if((people[start]+people[end])>limit):
            start = start + 1
        elif((people[start]+people[end])<=limit):
            del people[end]
            del people[start]
            start = 0
            end = len(people)-1
            answer = answer + 1
    return answer

print(solution([100,100],100))