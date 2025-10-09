# 로프
N = int(input())

ropes = [int(input()) for _ in range(N)]
ropes.sort(reverse=True)

max_weight = []

for i in range(N):
  max_weight.append(ropes[i]*(i+1))

print(max(max_weight))