# 약수 (브1)

N = int(input())
factor = list(map(int, input().split()))

factor.sort()

if N == 1:
  print(factor[0]*factor[0])
else:
  print(factor[0]*factor[N-1])