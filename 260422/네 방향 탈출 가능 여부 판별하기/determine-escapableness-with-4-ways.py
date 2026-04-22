from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[-1] * m for _ in range(n)]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        now_x, now_y = queue.popleft()

        for k in range(4):
            nx, ny = now_x + dx[k], now_y + dy[k]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == -1 and a[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = 1

    if visited[n-1][m-1] == 1:
        print(1)
    else:
        print(0)


        
bfs(0,0)
