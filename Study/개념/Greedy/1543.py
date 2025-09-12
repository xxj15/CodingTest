# 문서 검색 

string = str(input())
find_string = str(input())

ans = 0 
i = 0 

while i <= len(string) - len(find_string):
    idx = string.find(find_string, i)
    if idx == -1: 
        break
    ans += 1
    i = idx + len(find_string)
  
print(ans)
    