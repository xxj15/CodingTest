# 수 정렬하기 2

N = int(input())
numbers = []
for _ in range(N):
  numbers.append(int(input()))

numbers.sort()

print('\n'.join(map(str, numbers)))