# 경비원

w, h = map(int, input().split()) # 블록의 가로, 세로 길이 
s = int(input()) # 상점의 개수 
stores = []

def find_location(dir, dist): # (동서남북 방향, 떨어진 거리 입력받음) -> 원점에서 시계방향만큼 돌았을 때  거리 반환
  if dir == 1 :
    return h + dist
  elif dir == 2 : 
    return 2*h + 2*w - dist
  elif dir == 3:
    return h - dist
  else : 
    return h + w + dist
  
for i in range(s):
  x, y = map(int, input().split())
  stores.append(find_location(x,y))

x, y = map(int, input().split())
donggeun = find_location(x,y)

total_dist = 2 * (w+h)

ans = 0 

for store in stores:
  gap = abs(donggeun - store)
  ans += min(gap, total_dist - gap)

print(ans)
