# 최소, 최대 2

T= int(input())

def find_minmax(num_list):
  print(min(num_list), max(num_list))

for _ in range(T):
  N = int(input())
  numbers = list(map(int, input().split()))
  find_minmax(numbers)