height = []

def solution(height):
    sum = 0
    for i in range(len(height)):
        couple = height[i:]
        print(couple)
        for ps in range(len(couple)-1):
            '''if couple[0] > couple[1]:
                max = couple[0]
            else:'''
            max = couple[1]

            if max <= couple[ps]:
                sum += 1
                max = couple[ps]
                print('max=',max)
    print(sum)

if __name__ == "__main__":
    line = int(input())
    for _ in range(line):
        height.append(int(input()))

    solution(height)