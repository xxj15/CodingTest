# 임시 반장 정하기
import sys
input = sys.stdin.readline

N = int(input())
students = []

for i in range(N):
  row = list(map(int, input().split()))
  students.append(row)

classLeader = 0 
max_cnt = -1 

for i in range(N):
  cnt = 0
  for j in range(N):
    if i != j:
      for k in range(5):
        if students[i][k] == students[j][k] :
          cnt += 1
          break 
  if max_cnt < cnt: 
    max_cnt = cnt
    classLeader = i+1 

print(classLeader)

