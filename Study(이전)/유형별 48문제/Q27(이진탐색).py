# 정렬된 배열에서 특정 수의 개수 구하기 
from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
numbers = list(map(int, input().split()))

right = bisect_right(numbers, x)
left = bisect_left(numbers, x)

if right - left > 0 :
  print(right-left)
else:
  print(-1)