# 그룹 단어 체커 

N = int(input())
ans = N

for _ in range(N):
  word = list(input())
  for j in range(len(word)-1):
    if word[j] == word[j+1]:
      continue
    elif word[j] in word[j+2:]:
      ans -= 1
      break

print(ans)