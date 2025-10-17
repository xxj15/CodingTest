# 스택(실5)

N = int(input())
stack = []

for _ in range(N):
  command = input().split()
  if command[0] == 'push':
    stack.append(int(command[1]))
  elif command[0] == 'top':
    if stack:
      print(stack[-1])
    else:
      print(-1)
  elif command[0] == 'size':
    print(len(stack))
  elif command[0] == 'empty':
    if len(stack)==0:
      print(1)
    else:
      print(0)
  else : # pop 
    if stack:
      print(stack.pop())
    else:
      print(-1)