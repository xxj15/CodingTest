# 프린터 큐 (실3)
from collections import deque
T = int(input()) # 테스트 케이스 개수 

for _ in range(T):
  N, M = map(int, input().split())
  documents = list(map(int, input().split()))
  queue = deque()
  for (idx, priority) in enumerate(documents):
    queue.append((idx,priority)) # (인덱스, 중요도) 순서로 queue에 저장

  ans = 0 
  while queue:
    cur = queue.popleft() # 현재 있는것 추출
    max = 0 
    for others in queue:
      if others[1]>max:
        max = others[1]

    if cur[1]< max:
      queue.append(cur)
    else:
      ans += 1
      if cur [0] == M :
        print(ans)
        break

  