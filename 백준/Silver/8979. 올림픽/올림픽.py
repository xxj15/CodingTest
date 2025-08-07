#올림픽

n, k = map(int, input().split())
rows = []
for _ in range(n):
  row = list(map(int, input().split()))
  rows.append(row)

rows.sort(key=lambda x: [x[1],x[2], x[3]] , reverse=True)
rate = 1

for i in range(n):
  if i>0 and rows[i][1:] != rows[i-1][1:]:
    rate += 1
  
  if rows[i][0] == k:
    print(rate)
    break
