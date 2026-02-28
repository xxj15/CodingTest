from collections import deque
N, M = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# melt 함수  - 빙하 녹이기 
def melt():
  melt_amount = [[0] * M for _ in range(N)]
  for x in range(N):
        for y in range(M):
            if data[x][y] > 0:
                cnt_sea = 0 # 사방에 있는 바다 수 
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == 0:
                        cnt_sea += 1
                melt_amount[x][y] = cnt_sea

  for x in range(N):
    for y in range(M):
      if data[x][y] - melt_amount[x][y] >0:
        data[x][y] -= melt_amount[x][y]
      else:
        data[x][y] = 0


# bfs 함수 
# 빙하 두개로 쪼개지면 keep -1 리턴
def bfs(arr):
  visited = [[-1] * M for _ in range(N)] # visited 는 bfs 돌떄마다 -1로 초기화해야하니까 
  cnt = 0
  for x in range(1, N):
   for y in range(1, M):
    if arr[x][y] >=1 and visited[x][y] == -1:
      queue = deque([(x,y)])
      cnt += 1
      visited[x][y]=1
      while queue:
        now_x, now_y = queue.popleft()
        for k in range(4):
          nx, ny = now_x + dx[k], now_y + dy[k]
          if 1<=nx<N and 1<=ny<M and visited[nx][ny]==-1 and arr[nx][ny] >0:
            queue.append((nx, ny))
            visited[nx][ny]=1

  return cnt
  
years = 0 
while True:
  num_ice = bfs(data)
  if num_ice == 0:
    print(0)
    break
  elif num_ice>1: # 두개로 쪼개짐 
    print(years)
    break
  melt()
  years+=1
  bfs(data)