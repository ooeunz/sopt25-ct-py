N=int(input())
li=[] # n은 양수이며 11보다 작기 때문에 고정
li.extend([1,2,4]) # 1일때 2일때 3일때 경우의 수 입력
for i in range(3,11) : # 4 이상 부터는 (x-1) + (x-2) + (x-3) 각 경우의 수의 합이다
    li.append(li[i-1]+li[i-2]+li[i-3])
for _ in range(N) :
    num = int(input())
    print(li[num-1])