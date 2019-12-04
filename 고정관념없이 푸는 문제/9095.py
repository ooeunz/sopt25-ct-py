
t = int(input())
answer = 0
li= [0,1,2,4,0,0,0,0,0,0,0,0]
answer = 0
ans =[]
for _ in range(t):
    n = int(input())
    if n == 1 or n == 2 or n ==3:
        print(li[n])
    else:
        for i in range(4,n+1):
            li[i] = li[i-1] +li[i-2] +li[i-3]
            answer= li[i]
        print(answer)   