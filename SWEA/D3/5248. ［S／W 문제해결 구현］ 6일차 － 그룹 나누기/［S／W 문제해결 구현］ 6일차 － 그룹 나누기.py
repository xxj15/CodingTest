T = int(input())

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])

  return parent[x]

def union(a,b):
  root_a = find(a)
  root_b = find(b)

  if root_a != root_b:
    parent[root_b] = root_a

for tc in range(1,T+1):
  N, M = map(int, input().split())
  data = list(map(int, input().split()))
  parent = [i for i in range(N+1)]

  for i in range(0,M*2,2):
    union(data[i], data[i+1])

  ans = set()
  for i in range(1,N+1):
    ans.add(find(i))

  print(f"#{tc} {len(ans)}")