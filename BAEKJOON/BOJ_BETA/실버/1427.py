#소트 인사이드
import sys
input = sys.stdin.readline

numbers = list(map(int, input().strip()))
numbers.sort(reverse=True)

ans = ''.join(map(str,numbers))
print(ans)