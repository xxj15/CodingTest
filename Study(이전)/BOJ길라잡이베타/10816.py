#숫자카드 2
N = int(input())
have_cards = list(map(int, input().split()))

cnt = {}

for card in have_cards:
  if card in cnt:
    cnt[card]+=1
  else:
    cnt[card]=1


M = int(input())
check_cards = list(map(int, input().split()))
ans = []
for card in check_cards:
  if card in cnt:
    ans.append(cnt[card])
  else:
    ans.append(0)

print(*ans)

# dict는 내부적으로 hash table을 사용해서 1) key 존재 여부 확인 2) 값 접근
# 이 두 가지를 평균 O(1) 시간에 수행함. 