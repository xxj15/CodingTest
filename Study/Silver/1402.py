#아무래도이문제는A번난이도인것같다
import sys, math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  a, b = map(int, input().split())
  ans = 'no'
  if a == 0:
    ans = 'yes'

  else:  
    abs_a = abs(a)
    for num1 in range(1, int(abs_a**(0.5)) + 1):
       if abs_a % num1 == 0 : 
        num2 = abs_a // num1
        if a>0:
          if num1 + num2 == b or (-num1) + (-num2) == b:
            ans = 'yes'
            break
        else:
          if (-num1) + num2 == b or num1 + (-num2) == b:
            ans = 'yes'
            break  
  print(ans)  