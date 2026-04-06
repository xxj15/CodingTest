# 공유기 설치 
n, c = map(int, input().split())
homes = list(int(input()) for _ in range(n))
homes.sort()

start = 1
end = homes[-1]-homes[0]
ans = 0 

while(start <= end):
  mid = (start + end) // 2
  now_home = homes[0]
  cnt = 1

  for i in range(1, n):
    if homes[i] >= now_home + mid:
      now_home = homes[i]
      cnt += 1

  if cnt >= c:
    start = mid + 1
    ans = mid 
  else:
    end = mid - 1

print(ans)