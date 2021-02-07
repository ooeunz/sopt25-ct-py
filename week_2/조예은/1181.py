words = []

def solution(words):
    sortWords = sorted(set(words), key = lambda x: (len(x), x)) 
    return sortWords

if __name__ == "__main__":
    
    num = int(input())

    for i in range(num):
        words.append(input())
    ans = solution(words)
    
    for w in range(len(ans)):
        print(ans[w])

"""
def comp(s):
    return (len(s), s)

n = int(input())
arr = [input() for i in range(n)]
for i in sorted(set(arr), key=comp):
    print(i)

"""