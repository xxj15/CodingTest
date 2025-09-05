# 스위치 켜고 끄기 
N = int(input()) # 스위치 개수
switches = list(map(int, input().split()))

M = int(input()) # 학생 수
students = [list(map(int, input().split())) for _ in range(M)]

def toggle(i):
  switches[i] = (switches[i] + 1) % 2

for gender, num in students:
  if gender == 1 :
    for idx in range(num-1, N, num):
      toggle(idx)

  else: 
    center = num-1
    left, right = center -1, center +1 

    while left>= 0 and right <= N-1 and switches[left] == switches[right]: 
      left -= 1
      right += 1 
    
    for idx in range(left+1, right):
      toggle(idx)

for i in range(N):
  print(switches[i], end = ' ')
  if (i+1)%20 == 0 :
    print()