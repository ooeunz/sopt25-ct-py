def solution(line):
    
    sortLine = sorted(line)
    return int(sortLine[0]) * int(sortLine[2])

if __name__ == "__main__":
    line = input().split(' ')
    print(solution(line))

# 1
"""
inp = input()
inp = list(map(int,inp.split()))
inp.sort()

print(inp[0]*inp[2])
"""

# 2
"""
a,_,c,_=sorted(list(map(int,input().split())));print(a*c)
"""