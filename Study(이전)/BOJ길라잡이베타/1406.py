# 에디터
# 인덱스로 접근 : list > deque
# 양 끝에서 삽입,삭제 : list < deque
from collections import deque
left = deque(input())   
right = deque()   
cursor = 0 
N = int(input())

for _ in range(N):
  command = input().split()
  if command[0]=='L':
    if left:
      right.appendleft(left.pop())
  elif command[0]=='D':
    if right:
      left.append(right.popleft())
  elif command[0]=='B':
    if left:
      left.pop()
  else: # command[0] =='P'
    left.append(command[1])

print(''.join(left+right))
      
