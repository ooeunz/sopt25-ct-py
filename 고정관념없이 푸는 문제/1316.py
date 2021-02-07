import itertools
from collections import Counter
n = int(input())
answer =0
for _ in range(n):
    s = list(input())
    G = itertools.groupby(s) 
    an = [k for k, v in G] 
    # 여기서는 연속되면서 중복되는 것 제외하고 하나씩 만 나온다 .. 
    mode = Counter(an).most_common(1)
    if mode[0][1] == 1:
        answer += 1
print(answer)