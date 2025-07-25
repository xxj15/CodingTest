# 미로 탈출
# BFS 이용 - BFS는 가까운 곳부터 차례로 탐색하기 때문에, 도착점에 '처음 도달'했을 때의 경로가 항상 최단 경로가 된다. 
from collections import deque

N, M = map(int, input().split())

graph = []
for _ in range(N):
  graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x,y))
  
  # 시작점을 1로 설정 (이동 가능한 칸)
  graph[x][y] = 1

  while queue:
    x, y = queue.popleft()
    
    # 도착점에 도달했으면 최단 거리 반환 !!
    if x == N-1 and y == M-1:
      return graph[x][y]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx<0 or nx>=N or ny<0 or ny >= M: 
        continue

      # 이동 가능한 칸(1)일 때만 방문
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx,ny))

  return graph[N-1][M-1]

print(bfs(0,0))