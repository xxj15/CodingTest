# 좌표 정렬하기 2 (실5)
N = int(input())

points = []

for _ in range(N):
  x, y = map(int, input().split())
  points.append((x,y))

sort_points = sorted(points, key = lambda x : (x[1], x[0]))

for ans in sort_points:
  print(*ans)