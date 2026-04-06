# 못생긴 수

n = int(input())

numbers = [1]
i1, i2, i3 = 1, 1,1

for i in range(n):
  next1 = i1* 2
  next2 = i2 * 3
  next3 = i3 * 5

  if min(next1, next2, next3) == next1 :
    i1 += 1
  if min(next1, next2, next3) == next2 : 
    i2 += 1
  if min(next1, next2, next3) == next3: 
    i3 += 1

  numbers.append(min(next1, next2, next3))
  
print(numbers[n-1])
