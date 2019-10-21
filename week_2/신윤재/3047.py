def solution():
    abc = list(map(int, input().split()))
    orders = list(input())
    a, b, c = sorted(abc)
    
    ans = []
    for order in orders:
        if order == "A":
            ans.append(a)
        elif order == "B":
            ans.append(b)
        elif order == "C":
            ans.append(c)
    return ans

if __name__ == "__main__":
    ans = solution()
    print("{0} {1} {2}".format(ans[0], ans[1], ans[2]))


