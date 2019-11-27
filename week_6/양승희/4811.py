# n : 약의 개수 
# w : 한조각 꺼낸날 
# h : 반조각 꺼낸날 

# 1. w의 개수 - 알약의 개수보다 적게!!!
# 2. h의 개수 - w의 개수보다 작거나 같아야함!
# 3. 처음은 무조건 w! - ㅇㅇ
# 4. 탈출조건 - h이고, d 알약개수 0?1
# 5. 탈출조건 완성되면, total_cnt ++ 

case = list()
total_cnt = 0

def solution(cnt, w, h): 
    global total_cnt
    if w == 0 and h == 0 :
        print("*1")
        return solution(cnt, 1, 0)
    
    # W 하나
    if w < cnt :
        print("*2")
        w += 1  
        return solution(cnt, w, h)

    # H 절반
    if h < w :
        print("*3")
        # 탈출 조건
        if w == cnt : 
            print("*4")
            total_cnt += 1
        else:
            h += 1    
            return solution(cnt, w, h)

while(True):
    input_str = int(input())

    if input_str == 0 :
        break

    total_cnt = 0
    solution(input_str, 0, 0)
    print(total_cnt)
