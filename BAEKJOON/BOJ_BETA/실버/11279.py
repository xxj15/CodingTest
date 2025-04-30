# 최대 힙 
import sys, heapq 
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if (x == 0):
        if (len(heap) == 0):
            print(0)
        else :
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-x,x)) # (priorty, value) 값을 heap 에 넣기 
