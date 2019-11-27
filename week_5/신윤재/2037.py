push, wait = map(int, input().split())
words = input()
ans = 0

def check_same_group(word):
    if word == 'A' or word == 'B' or word == 'C':
        return ['A', 'B', 'C']
    elif word == 'D' or word == 'E' or word == 'F':
        return ['D', 'E', 'F']
    elif word == 'G' or word == 'H' or word == 'I':
        return ['G', 'H', 'I']
    elif word == 'J' or word == 'K' or word == 'L':
        return ['J', 'K', 'L']
    elif word == 'M' or word == 'N' or word == 'O':
        return ['M', 'N', 'O']
    elif word == 'P' or word == 'Q' or word == 'R' or word == 'S':
        return ['P', 'Q', 'R', 'S']
    elif word == 'T' or word == 'U' or word == 'V':
        return ['T', 'U', 'V']
    elif word == 'W' or word == 'X' or word == 'Y' or word == 'Z':
        return ['W', 'X', 'Y', 'Z']
    else:
        return []

alphabet = {
    'A':1, 'B':2, 'C':3, 
    'D':1, 'E':2, 'F':3, 
    'G':1, 'H':2, 'I':3, 
    'J':1, 'K':2, 'L':3, 
    'M':1, 'N':2, 'O':3, 
    'P':1, 'Q':2, 'R':3, 'S':4,
    'T':1, 'U':2, 'V':3,
    'W':1, 'X':2, 'Y':3, 'Z':4,
    ' ':1
    }
past_word = []
for word in words:
    ans += alphabet[word] * push
    if word in past_word:
        ans += wait
    past_word = check_same_group(word)

print(ans)