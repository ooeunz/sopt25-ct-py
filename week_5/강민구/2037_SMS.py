button, rest = map(int,input().split()) # button = 입력 시간 , rest = 같은 숫자 연속입력 시 기다리는 시간
result = 0
check = 0
text = list(input())
al_dic = {
          2 : ['A', 'B', 'C'],
          3 : ['D', 'E', 'F'],
          4 : ['G', 'H', 'I'],
          5 : ['J', 'K', 'L'],
          6 : ['M', 'N', 'O'],
          7 : ['P', 'Q', 'R', 'S'],
          8 : ['T', 'U', 'V'],
          9 : ['W', 'X', 'Y', 'Z']}
# al_dic = {'A' : 1,'B' : 2, 'C' : 3 ,
#           'D' : 1, 'E' : 2, 'F' : 3,
#           'G' : 1 , 'H' : 2, 'I' : 3,
#           'J' : 1, 'K' : 2, 'L' : 3,
#           'M' : 1, 'N' : 2, 'O' : 3,
#           'P' : 1, 'Q' : 2, 'R' : 3, 'S' : 4,
#           'T' : 1, 'U' : 2, 'V' : 3,
#           'W' : 1, 'X' : 2, 'Y' : 3, 'Z' :4}
# for i in range(len(text)) :
#     # A ~ C
#     if text[i] >= 'A' and text[i] <= 'C' :
#         result += button * al_dic[text[i]]
#         if check == 1 :
#             result += rest
#         check = 1
#
#     # D ~ F
#     elif text[i] >= 'D' and text[i] <= 'F' :
#         result += button * al_dic[text[i]]
#         if check == 2 :
#             result += rest
#         check = 2
#
#     # G ~ I
#     elif text[i] >= 'G' and text[i] <= 'I' :
#         result += button * al_dic[text[i]]
#         if check == 3 :
#             result += rest
#         check = 3
#
#     # J ~ L
#     elif text[i] >= 'J' and text[i] <= 'L' :
#         result += button * al_dic[text[i]]
#         if check == 4 :
#             result += rest
#         check = 4
#
#     # M ~ O
#     elif text[i] >= 'M' and text[i] <= 'O' :
#         result += button * al_dic[text[i]]
#         if check == 5 :
#             result += rest
#         check = 5
#
#     # P ~ S
#     elif text[i] >= 'P' and text[i] <= 'S' :
#         result += button * al_dic[text[i]]
#         if check == 6 :
#             result += rest
#         check = 6
#
#     # T ~ V
#     elif text[i] >= 'T' and text[i] <= 'V' :
#         result += button * al_dic[text[i]]
#         if check == 7 :
#             result += rest
#         check = 7
#
#     # W ~ Z
#     elif text[i] >= 'W' and text[i] <= 'Z' :
#         result += button * al_dic[text[i]]
#         if check == 8 :
#             result += rest
#         check = 8
#
#     else :
#         result += button
#         check = 0

for alpha in text :
    count = [number for number, chars in al_dic.items() if alpha in chars] # 해당 문자가 있는 키 값 전달
    if not count : # 공백일 경우
        result += button
        check = 0
    else :
        # 문자가 위치한 인덱스를 찾아 +1을 하면 그것이 곧 연속적으로 입력해야하는 횟수가 된다
        t = [c for c in range(len(al_dic[count[0]])) if alpha == al_dic[count[0]][c]]
        if check == count : # 이전 문자와 비교
            result += rest + button*(t[0]+1)
        else :
            result += button*(t[0]+1)
        check = count
print(result)