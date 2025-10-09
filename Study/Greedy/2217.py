# 로프
N = int(input())

ropes = [int(input()) for _ in range(N)]
ropes.sort(reverse=True)

max_weight = []

for i in range(N):
  max_weight.append(ropes[i]*(i+1))

print(max(max_weight))

# 아이디어 : (가장 약한 로프의 최대 하중 × 사용한 로프의 개수) = 전체가 들 수 있는 무게 
# 사용한 알고리즘 : Greedy