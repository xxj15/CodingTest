#음료수 얼려먹기 
N, M = map(int, input().split()) # 세로, 가로 길이 

# 그래프 입력받기 
graph = []
for _ in range(N):
  graph.append(list(map(int, input())))

# dfs 구현 
def dfs(x, y):
  # dfs는 재귀니까 종료조건 필요 
  if x<0 or x>=N or y <0 or y>=M :
    return False

  # 방문하지 않음 
  if graph[x][y] == 0:
    graph[x][y] = 1 

    # 상하좌우 탐색 
    dfs (x-1, y)
    dfs (x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)

    return True
  
  # 이미 방문했거나 벽 
  else:
    return False
  

result = 0
for i in range(N):
  for j in range(M):
    if dfs(i, j):
      result += 1

print(result)

