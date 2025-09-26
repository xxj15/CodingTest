# 넷이 놀기 

N = int(input())
A, B = map(int, input().split())
pts = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0

for x, y in pts:
  if (x+A, y) in pts and (x+A, y+B) in pts and (x, y+B) in pts :
    ans += 1

print(ans)





# # 넷이 놀기 - Brute Force 코드 
# import itertools
# from collections import Counter

# N = int(input())
# A, B = map(int, input().split())
# spots= []
# ans = 0 

# for _ in range(N):
#   x, y = map(int, input().split())
#   spots.append([x,y])

# for spot_comb in itertools.combinations(spots,4):
#   xs = [x for x, _ in spot_comb]
#   ys = [y for _, y in spot_comb]

#   cx, cy = Counter(xs), Counter(ys)

#   if sorted(cx.values()) == [2,2] and sorted(cy.values()) == [2,2]: # 직사각형 후보 
#     if (max(xs)- min(xs) == A) and (max(ys)- min(ys) == B):
#       ans += 1

# print(ans)
    