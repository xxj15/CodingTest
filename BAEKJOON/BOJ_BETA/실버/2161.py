#카드1
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())  # 카드 개수
cards = deque(range(1, n + 1))
discard_cards = []

while len(cards) > 1:
    discard_cards.append(cards.popleft())  
    cards.append(cards.popleft())   

for card in discard_cards:
  print(card, end =' ')

print(cards[0])
