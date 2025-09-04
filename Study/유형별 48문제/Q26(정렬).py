# 카드 정렬하기 
import heapq

N = int(input())
heap = []

for _ in range(N): 
  number = int(input())
  heapq.heappush(heap, number) # 데이터 힙에 삽입하기 

ans = 0 

while len(heap) >= 2: 
  a = heapq.heappop(heap)
  b = heapq.heappop(heap)

  sum = a+b
  ans += sum
  heapq.heappush(heap, sum)

print(ans)