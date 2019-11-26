number = int(input())
problem = []
for _ in range(number):
    deadline,cup = input().split(" ")
    deadline = int(deadline)
    cup = int(cup)
    problem.append((deadline,cup))
problem = sorted(problem,key=lambda problem: problem[0])
big = 0
result = 0
basic = -1
order = -1
for i in range(len(problem)):
    basic = problem[i][0]
    if(basic is not order):
        result = result + big
        big = 0
        if(problem[i][1]>big):
            big = problem[i][1]
    else:
        if(problem[i][1]>big):
            big = problem[i][1]
    order = problem[i][0]
    if(i == (len(problem)-1)):
        result = result + big
print(result)
