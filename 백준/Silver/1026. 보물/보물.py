# 보물(실4)
N = int(input())

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

listA.sort()
listB.sort(reverse=True)
ans = 0 
for i in range(N):
  ans += listA[i]*listB[i]

print(ans)