# N과 M(7)
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

def call(answer, depth):
  if depth == M : 
    print(' '.join(map(str, answer)))
    return 
  
  for i in range(len(numbers)):
    answer.append(numbers[i])
    call(answer, depth + 1)
    answer.pop()
    

for num in numbers:
  ans = [num]
  call(ans, 1)