#기타줄 
import math
n, m = map(int, input().split())

groups = []
single = []

for i in range(m):
  x, y = map(int, input().split())
  groups.append(x)
  single.append(y)

min_group = min(groups) # 6개 그룹으로 구매할 경우 가장 낮은 가격
min_single = min(single) # 낱개로 구매할 경우 가장 낮은 가격

M = math.ceil(n / 6) # 6개 묶음으로 구매할 수 있는 최대 양 (묶음 수)
cost = min_group * M

for i in range(M):
  if 6* i < n : 
    buy = n - 6*i
  else:
    buy = 0

  cost = min(cost, buy * min_single + i * min_group)

print(cost)



