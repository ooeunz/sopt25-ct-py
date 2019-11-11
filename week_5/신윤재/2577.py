import sys
from collections import Counter

abc = [int(sys.stdin.readline()) for _ in range(3)]
num = str(abc[0] * abc[1] * abc[2])
counter = dict(Counter(list(str(num))))

for idx in range(0, 10):
    if str(idx) in counter.keys():
        print(counter[str(idx)])
    else:
        print("0")


