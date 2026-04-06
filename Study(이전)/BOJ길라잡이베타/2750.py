# 수 정렬하기 (브2)

N = int(input())
numbers = []
for _ in range(N):
  numbers.append(int(input()))

numbers.sort()

print(*numbers, sep='\n')