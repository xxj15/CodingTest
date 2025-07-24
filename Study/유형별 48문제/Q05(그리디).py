# 볼링공 고르기 

n, m = map(int, input().split())
balls = list(map(int, input().split()))

cnt = 0 

for a in range(len(balls)-1) : 
  for b in range(a+1, len(balls)) : 
    if balls[a]!=balls[b]:
      cnt +=1

print(cnt)