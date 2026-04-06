#큰수의 법칙
import sys 
input = sys.stdin.readline 

N, M, K = map (int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

max = numbers[-1]
second_max = numbers [-2]

result = 0 

while True:
  for i in range(K):
    if M == 0:
      break
    result += max
    M -= 1 
  if M == 0 :
    break

  result += second_max
  M -= 1

print(result)

