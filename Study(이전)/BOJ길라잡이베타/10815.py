# 숫자카드 (실5)
# list로 시간초과나면 set을 이용할 수 있는지 생각해보자
N = int(input())
cards = set(map(int, input().split()))

M = int(input())
check_nums = list(map(int, input().split()))

ans = []
for number in check_nums:
  if number in cards:
    ans.append(1)
  else:
    ans.append(0)

print(*ans)