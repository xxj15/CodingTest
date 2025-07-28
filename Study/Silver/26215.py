# 눈 치우기 
import sys, heapq
input = sys.stdin.readline

queue = []

N = int(input())
homes = list(map(int, input().split()))

for i in range(N): 
  heapq.heappush(queue, (-homes[i], i+1))

cnt = 0 

if max(homes) > 1440 : 
  print(-1)

else:
  while queue:
    if len(queue) >= 2 : 
      snow1, idx1 = heapq.heappop(queue)  
      snow1 += 1  
      snow2, idx2 = heapq.heappop(queue)  
      snow2 += 1
      if snow1 < 0:
        heapq.heappush(queue, (snow1, idx1))
      if snow2 <0 :
        heapq.heappush(queue, (snow2, idx2))
      cnt += 1
      
    else: 
      snow, idx = heapq.heappop(queue)
      snow += 1
      if snow<0:
        heapq.heappush(queue, (snow, idx))
      cnt += 1

  if cnt > 1440:
    print(-1)
  else: 
    print(cnt)

