# 위에서 아래로 
import sys
input = sys.stdin.readline

N = int(input())
numbers = []

for _ in range(N):
  numbers.append(int(input()))

numbers.sort(reverse=True)

for number in numbers:
  print(number, end = " ")