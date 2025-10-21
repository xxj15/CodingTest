# 좌표 정렬하기 (실5)
N = int(input())
points=[]

for _ in range(N):
  x, y = map(int, input().split())
  points.append((x,y))

sort_list = sorted(points, key = lambda s: (s[0], s[1]))

for ans in sort_list:
  print(*ans)
