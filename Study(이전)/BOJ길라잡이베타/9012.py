# 괄호 (실4)
N = int(input())

for _ in range(N):
  stack = []
  data = input().strip()
  for x in data:
    if x == '(':
      stack.append(x)
    else: # x == ')'
      if not stack:
        print("NO")
        break
      else:
        stack.pop()

  else:
    print("NO" if stack else "YES")
   
