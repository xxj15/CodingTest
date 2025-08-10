# 마라톤 틱택토 

N = int(input())
board = []

for i in range(N):
  board.append(list(input()))

# 오른쪽, 오른쪽 아래, 아래, 왼쪽 아래 - 네 가지 방향 확인 
dirs = [(0,1), (1,1), (1,0), (1,-1)]


for i in range(N):
  for j in range(N): 
    if board[i][j] == '.':
      continue

    else: 
      for dx, dy in dirs: 
        check = True
        for step in range(1, 3): # 세칸 연속인지 확인
          nx = i + dx * step 
          ny = j + dy * step 

          # 경계 넘거나 연속되지 않음을 발견할 시 break 
          if not (0 <= nx < N and 0 <= ny < N) or board[i][j] != board[nx][ny]:
            check = False
            break 

        if check : 
          print(board[i][j])
          exit()

print('ongoing')