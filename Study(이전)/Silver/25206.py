# 너의 평점은 
import sys 
input = sys.stdin.readline

grades = ['A+', 'A0', 'B+','B0','C+','C0','D+','D0','F']
scores = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0]

tot_credit = 0 # 학점 수  
tot_score = 0 # 점수 합계 

for i in range(20):
  x = list(map(str, input().split()))
  if x[2] == 'P' :
    continue
  else:
    credit = float(x[1])
    tot_credit += credit
    idx = grades.index(x[2])
    tot_score += float(scores[idx] * credit)


ans = float(tot_score / tot_credit)
print(format(ans, ".6f"))



