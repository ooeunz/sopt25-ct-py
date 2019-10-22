T = int(input())
words = [] # 입력받은 단어를 넣을 리스트
sorts =[] # [길이,단어] 순으로 넣을 리스트

for _ in range(T) :
    word = input()
    words.append(word)

# 중복 제거
words= list(set(words))

# 리스트에 [단어 길이, 단어] 형식으로 저장
for word in words :
    sorts.append((len(word),word))

sorts.sort() # 이중 리스트 일 때, 앞에 요소로 정렬 후 동일할 시 뒤에 요소로 정렬

# 길이는 말고 단어만 출력
for len, word in sorts :
    print(word)




