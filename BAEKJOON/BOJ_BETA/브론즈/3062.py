# 수 뒤집기
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  s = str(input())
  n = str(int(s)+ int(s[::-1]))

  if n == n[::-1]:
    print("YES")
  else:
    print("NO")