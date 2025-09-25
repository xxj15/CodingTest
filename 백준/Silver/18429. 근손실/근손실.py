# 근손실
import itertools, math

N, K = map(int, input().split())
kits = list(map(int, input().split()))
start = 500 
ans = math.factorial(N)

for new_kits in itertools.permutations(kits, N):
  weight = start
  for kit in new_kits:
    weight += kit - K 
    check = True
    if weight < 500:
      check = False
      ans -= 1
      break

print(ans)