
def solution(arr1, arr2):

    arr1.sort()
    arr2.sort(reverse=True)

    ans = sum(map(lambda n: n[0] * n[1], zip(arr1, arr2)))
    print(zip(arr1, arr2))
    return ans

if __name__ == "__main__":

    length = int(input())
    a_arr = list(map(int, input().split(' ')))
    b_arr = list(map(int, input().split(' ')))
    
    #print(solution(a_arr, b_arr))