# 4659번 비밀번호 발음하기 
import sys
input = sys.stdin.readline

def check(word):
    vowels = {'a','e','i','o','u'}
    cnt_v = 0
    cnt_c = 0
    if not (vowels & set(word)):
        return -1
    
    
    for w in data:
        if cnt_c == 3 or cnt_v == 3 :
            return -1 
        if w in vowels:
            if cnt_c !=0:
                cnt_c = 0
            cnt_v += 1
        else:
            if cnt_v != 0:
                cnt_v = 0
            cnt_c += 1

    if cnt_c == 3 or cnt_v == 3 :
        return -1 
    
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            if word[i] =='e' or word[i]=='o':
                continue
            else:
                return -1
    
    else:
        return 1
        



while True:
    data = input().rstrip()
    if data == 'end':
        break

    ans = check(data)
    if ans == 1:
        print(f"<{data}> is acceptable.")
    else:
        print(f"<{data}> is not acceptable.")