#요세푸스 문제
from collections import deque
N, K = map(int, input().split())

queue = deque(range(1, N+1))
ans = []

while queue:
  queue.rotate(-(K-1))
  pop_num = queue.popleft()
  ans.append(str(pop_num))

print("<" + ", ".join(ans) + ">")



