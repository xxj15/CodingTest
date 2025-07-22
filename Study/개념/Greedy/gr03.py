#숫자 카드 게임
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
answer = 0

for i in range(N):
  numbers = list(map(int, input().split()))
  min_number = min(numbers)

  answer = max(min_number, answer)

print(answer)