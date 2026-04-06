# 모험가 길드 
import sys
input = sys.stdin.readline

N = int(input())

group = list(map(int, input().split()))

count = 0 
ans = 0

for i in group:
  count += 1

  if count >= i :
    count = 0 
    ans += 1

print(ans)