result = {0 : "E", 1 : "A", 2 : "B" , 3 : "C" , 4 : "D"}
for _ in range(3) :
    yut = list(map(int, input().split()))
    print(result[yut.count(0)])
