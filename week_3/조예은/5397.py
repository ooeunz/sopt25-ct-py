passwords = []

def solution(passwords):
    for password in passwords:
        key = []
        subkey = []
        for word in password:
            if word is '<':
                if key:
                    subkey.append(key.pop())
            elif word is '>' :
                if subkey:
                    key.append(subkey.pop())
            elif word is '-':
                if key:
                    key.pop()
            else:
                key.append(word)
        print(''.join(key))
        

if __name__ == "__main__":
    num = int(input())

    for _ in range(num):
        inp = list(input())
        passwords.append(inp)
        
    solution(passwords)