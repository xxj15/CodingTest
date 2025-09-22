# 아이폰 9S

N = int(input())
people_line = [int(input()) for _ in range(N)]
people_type = set(people_line)
ans = 0

def check(arr):
  cnt = 1
  max_cnt = 1
  for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
      cnt += 1
    else: 
      max_cnt = max(cnt, max_cnt)
      cnt = 1
  return max(cnt, max_cnt)

for i in people_type:
  # people_line.remove(i) 로 하면 people_line 리스트 자체가 바뀌니까 사용 x + remove(i)는 리스트 안에 있는 i의 첫 번째 원소만 제거함
  new_line = [x for x in people_line if x != i]
  ans = max(ans, check(new_line))

print(ans)
