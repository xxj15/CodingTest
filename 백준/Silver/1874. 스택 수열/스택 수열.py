# 스택수열 (실2)
n = int(input())

sequence = [int(input()) for _ in range(n)] 
stack = []
ans = []
current = 1

for i in sequence:
  while current <= i :
    stack.append(current)
    ans.append("+")
    current += 1
  
  if stack[-1] == i:
    stack.pop()
    ans.append("-")
  
  else:
    print("NO")
    break

else:
  for x in ans:
    print(x)
