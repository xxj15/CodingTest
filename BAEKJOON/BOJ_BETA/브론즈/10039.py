# 평균 점수
import sys
input = sys.stdin.readline
sum = 0 

for _ in range(5):
  score = int(input())
  if score >= 40: 
    sum += score
  else: 
    sum += 40

print(sum//5)