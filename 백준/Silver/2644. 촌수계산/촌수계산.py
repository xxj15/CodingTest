# 촌수 계산
n = int(input()) # 전체 사람의 수 
a, b = map(int, input().split()) # 두 사람
m = int(input()) # 부모 자식들 간의 관계의 개수 

# 가족관계 넣어두기 
family = [[] for _ in range(n+1)]
for i in range(m):
  x, y = map(int, input().split())
  family[x].append(y)
  family[y].append(x)

visited = [False for _ in range(n+1)]
result = -1 
# dfs 로 계산 - 몇 번 dfs로 파고 들어가는지를 계산하면 촌수가 됨.
def dfs(x, cnt): 
  global result
  visited[x] = True
  if x == b:
    result = cnt 
    return
  for next_person in family[x]:
    if visited[next_person] == False:
      dfs(next_person, cnt + 1)

dfs(a, 0)
print(result)