T = int(input())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
  root_a, root_b = find(a), find(b)
  if root_a == root_b:
    return False 
  parent[root_b] = root_a
  return True  

for tc in range(1, T+1):
    V, E = map(int, input().split())
    parent = [i for i in range(V+1)]
    edges = []

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges.append((w, n1, n2))

    edges.sort()   
    ans, cnt = 0,0

    for w, n1, n2 in edges:
        if union(n1, n2):  
            ans += w
            cnt += 1
            if cnt == V: 
                break

    print(f'#{tc} {ans}')