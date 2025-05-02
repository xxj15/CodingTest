# 절댓값 힙
import sys, heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if (x == 0):
        if (len(heap)== 0):
            print(0)
        else :
            print(heapq.heappop(heap)[1]) # 튜플의 두번째 값 꺼냄

    else: # 이렇게 안하고 heapq.heappush(heap, (abs(x), x)) 로 해도 동일 
        if x>0 :
            heapq.heappush(heap, (x, x)) # (우선순위, 실제값) 형태의 튜플을 힙에 삽입 
        else :
            heapq.heappush(heap, (-x,x))