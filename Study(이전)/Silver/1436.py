# 영화감독 숌
import sys
input = sys.stdin.readline

n = int(input())

cnt = 0 
number = 666

while True:
  if '666' in str(number):
    cnt += 1

  if cnt == n :
    break

  number += 1

print(number)