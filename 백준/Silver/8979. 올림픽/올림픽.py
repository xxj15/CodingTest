#올림픽

n, k = map(int, input().split())
rows = []
for _ in range(n):
  row = list(map(int, input().split()))
  rows.append(row)

rows.sort(key=lambda x: [x[1],x[2], x[3]] , reverse=True)
pre_gold, pre_silver, pre_bronze = rows[0][1], rows[0][2], rows[0][3]
rate = 0

for row in rows : 
  if row[0] == k:
    if [row[1], row[2], row[3]] == [pre_gold,pre_silver, pre_bronze]:
      print(rate)
      break 
    else: 
      rate += 1
      print(rate)
      break
  else:
    if [row[1], row[2], row[3]] == [pre_gold,pre_silver, pre_bronze]:
      continue
    else: 
      rate += 1

