# 로또(실2)
from itertools import combinations

while True:
  input_numbers = list(map(int, input().split()))
  if input_numbers[0]== 0:
    break

  k, S = input_numbers[0], input_numbers[1:]

  for comb in combinations(S, 6):
    print(*comb)
  print()



