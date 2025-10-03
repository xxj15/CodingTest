# 점프 점프 

X, Y, P1, P2 = map(int,  input().split())  # 두 사람이 한 번에 멀리뛰기를 하는 거리 X, Y와 시작 지점의 위치 값 P1, P2
cnt = 0 
while True: 
  cnt += 1
  if P1 == P2: 
    print(P1)
    break
  if cnt > 10000:
    print(-1)
    break 
  elif P1 > P2 : 
    P2 += Y
  else:
    P1 += X





