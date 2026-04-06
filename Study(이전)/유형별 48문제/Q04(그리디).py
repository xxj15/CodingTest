# 만들 수 없는 금액 

N= int(input())
numbers = list(map(int, input().split()))
numbers.sort()

target = 1

for num in numbers: 
  if target < num : 
    break 

  target += num 

print(target)
