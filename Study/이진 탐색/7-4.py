#떡볶이 떡 만들기 (파라메트릭 서치)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))

start = 0 
end = max(array)

result = 0 
while(start<=end):
  total = 0 

  mid = (start+end)//2

  for x in array: 
    if x > mid : 
      total += x - mid

  if total < M :  # 떡의 양이 부족한 부분 - 덜 잘라야 함
    end = mid -1 

  else: 
    result = mid 
    start = mid + 1

print(result)

print(17//2)