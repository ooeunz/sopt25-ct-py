def solution(paper_list,h):
    paper_list.sort()
    for i in range(h) :
        if paper_list[i] >= h-i :
            answer = h-i
            return answer
            
for x in range(int(input())):
    print("case#"+str(x+1), end='')

    cnt = int(input())
    paper_list = list(input())
    #paper_list = list(map(int, paper_list))
    print(paper_list)

    for y in range(cnt):
        print( solution(paper_list,int(y+1)) , end='')
