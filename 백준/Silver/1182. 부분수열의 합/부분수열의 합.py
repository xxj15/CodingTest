#  부분수열의 합
from itertools import combinations

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
ans = 0

for i in range(1, N+1):
  for comb in combinations(numbers,i):
    if sum(comb)== S:
      ans += 1

print(ans)