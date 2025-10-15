N = int(input())
including_numbers = set(map(int, input().split()))
M = int(input())
find_numbers = list(map(int, input().split()))


for num in find_numbers:
  print(1 if num in including_numbers else 0)