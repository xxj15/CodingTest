# 나무꾼 이다솜
N, C, W = map(int, input().split()) # 나무의 개수, 나무 자를 때 드는 비용, 나무 한 단위의 가격

trees = [int(input()) for _ in range(N)]
max_tree = max(trees)
ans = 0 

for length in range(1, max_tree + 1):
  total = 0 
  for tree in trees : 
    if tree < length :
      continue
    number = tree // length 
    cutting_number = number -1 if (tree % length == 0) else number 
    profit = number * length * W - cutting_number * C

    if profit > 0 :
      total += profit

  ans = max(total, ans)


print(ans)

