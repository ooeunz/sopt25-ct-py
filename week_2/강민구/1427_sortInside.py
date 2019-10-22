Input=int(input())

numbers = [] # 입력받은 수를 내림차순 하기 위한 리스트

# 입력받은 수를 하나 씩 리스트에 넣기
while True :
    if(Input != 0) :
        number = int(Input%10)
        numbers.append(number)
        Input = int(Input/10)
    else :
        break

numbers.sort(reverse=True) # 내림차순 정렬
numbers=list(map(str,numbers)) # 리스트를 합치기 위해서 문자열 자료형으로 변경
result =int( "".join(numbers)) # 합친 다음 다시 int형으로 반환
print(result)
