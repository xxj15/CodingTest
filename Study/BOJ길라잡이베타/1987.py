# 소수 찾기 (브2)

N = int(input())
numbers = list(map(int, input().split()))
ans = 0

for num in numbers:
  if num == 1: 
    continue 
  else:
    is_prime = True

    for x in range(2, int(num ** 0.5 + 1)):
      if num % x == 0:
        is_prime = False
        break

    if is_prime == True:
      ans += 1

print(ans)