# BFS - 큐 자료구조 이용. 일반적인 경우 DFS보다 BFS가 수행시간이 더 빠름 

from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start]=True # 현재 노드를 방문처리 

  while queue: #큐가 빌때까지 반복
    v = queue.popleft()
    print(v, end=' ')
    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입 
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True





graph=[
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited=[False]*9

bfs(graph, 1, visited)