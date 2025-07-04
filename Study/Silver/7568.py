# 덩치 
import sys
input = sys.stdin.readline

N = int(input())
group = []
ans = []

for _ in range(N):
  weight, height = map(int, input().split())
  group.append((weight, height))

for i in range(N):
  cnt = 0 
  for j in range(N):
    if group[i][0] < group[j][0] and group[i][1] < group[j][1]:
      cnt +=1 
  ans.append(cnt+1)

for x in ans:
  print(x, end = " ")
    