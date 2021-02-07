# 알약 반쪽 한쪽 재귀 

import sys

pill = {}
answer = []
def solution(w, h):
    if (w,h) in pill:
        return pill[(w,h)]
    elif w is 0:
        return 1
    elif w <= h:
        pill[(w,h)] = solution(w-1, h) + solution(w, h-1)
        return pill[(w,h)]
    else:
        return 0
        

while True:
    n = int(sys.stdin.readline())
    if n is 0: break
    answer.append(solution(n,n))

print('\n'.join(map(str, answer))) 


    