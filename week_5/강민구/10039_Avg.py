import sys

def pointUp() :
    return 40

if __name__ == "__main__" :
    point=list(sys.stdin.readline().strip() for _ in range(5))
    point = list(map(int,point))

    for i in range(5) :
        if(point[i] < 40) :
            point[i] = pointUp()

    print(sum(point)//5)