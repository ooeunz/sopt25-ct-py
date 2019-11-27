import sys


def solution(ropes):
    ropes.sort(reverse=True)
    weight = 0

    for idx, rope in enumerate(ropes):
        if rope * (idx + 1) > weight:
            weight = rope * (idx + 1)
    return weight
     
if __name__ == "__main__":
    K = int(sys.stdin.readline())
    ropes = [int(sys.stdin.readline()) for _ in range(K)]
    
    print(solution(ropes))

