#왕실의 나이트 
import sys 
input = sys.stdin.readline

first = input()
row = int(first[1])
column = int(ord(first[0]))- int(ord(('a'))) + 1 

ans = 0 
steps = [(-1, -2), (-1,2), (1, -2), (1, 2),(-2, -1), (-2, 1), (2,-1), (2,1)]

for step in steps:
  n_row = row + step[0]
  n_column = column + step[1]

  if 1<=n_row<=8 and 1<=n_column<=8:
    ans += 1

print(ans)