# 고정점 찾기 
# 시간복잡도 O(logN)으로 알고리즘 설게하지 않으면 '시간초과'

# 재귀 함수 구현 
def binary_search (array, start, end):
  if start > end :
    return -1
  
  mid = (start + end) // 2 

  if array[mid] == mid:
    return mid 
  elif array[mid] > mid : 
    return binary_search(array, start, mid-1)
  else: 
    return binary_search(array, mid+1, end)


n = int(input())
numbers = list(map(int, input().split()))

idx = binary_search(numbers, 0, n-1)

if idx  :
  print(idx)
else:
  print(-1)