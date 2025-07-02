#상하좌우 - 시뮬레이션 
import sys
input = sys.stdin.readline

N = int(input())
moving = input().split()
x, y = 1, 1

#L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for move in moving:
  for i in range(4):
    if move == move_type[i]:
      nx = x + dx[i]
      ny = y + dy[i]

  if nx < 1 or ny < 1 or nx > N or ny > N : 
    continue

  x, y = nx, ny

print(x,y)