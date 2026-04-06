# 거스름돈

N = int(input())

money_list = [500, 100, 50, 10, 5, 1]
ans = 0
change = 1000-N

for money in money_list: 
  ans += change // money
  change %= money

print(ans)