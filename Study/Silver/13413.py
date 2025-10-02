# 오셀로 재배치
import math
T = int(input())

def check(first_str, goal_str):
  to_white=0
  to_black=0

  for f, g in zip(first_str, goal_str): # zip 함수
    if f != g:
      if f == 'B' and g == 'W':
        to_white+=1
      else:
        to_black+= 1
  return max(to_black, to_white)
    

for _ in range(T):
  N = int(input())
  first =input()
  goal =input()
  print(check(first, goal))

