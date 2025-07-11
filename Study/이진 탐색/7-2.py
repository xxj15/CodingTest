# 부품 찾기 
import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
  while start<= end: 
    mid = (start+end)//2

    if array[mid]==target:
      return mid
    
    # 중간값이 찾고자 하는 값보다 큰 경우 -> 중간값 기준 왼쪽 확인
    elif array[mid]>target: 
      end = mid - 1 

    else :
      start = mid + 1

  return None


N = int(input())
store = list(map(int, input().split()))
store.sort() 

M = int(input())
customer = list(map(int, input().split()))


for i in customer : 
  result = binary_search(store, i, 0, N-1)

  if result != None:
    print("yes", end=' ')

  else: 
    print("no", end=' ')