# 단어 뒤집기
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  line = list(input().split()) # I am happy today -> ['I', 'am', 'happy', 'today']
  
  for word in line:
    print(word[::-1], end = ' ')
  print()