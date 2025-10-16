#수 정렬하기 3

N = int(input())

isNumbers = [0]*10001

for _ in range(N):
  num = int(input())
  isNumbers[num] += 1

for i in range(10001):
  if isNumbers[i]!= 0:
    for _ in range(isNumbers[i]):
      print(i)