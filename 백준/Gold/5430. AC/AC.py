# AC (골드5)
from collections import deque

T = int(input())

for _ in range(T):
    p = list(input().strip())
    n = int(input().strip())
    numbers_str = input().strip()

    if numbers_str == "[]":
        numbers = deque()
    else:
        numbers = deque(int(x) for x in numbers_str[1:-1].split(','))

    is_reversed = False

    while True:
        if p.count('D') > n:
            print('error')
            break
        else:
            for cmd in p:
                if cmd == 'R':
                    is_reversed = not is_reversed
                else:
                    if is_reversed:
                        numbers.pop()
                    else:
                        numbers.popleft()
            if is_reversed:
                numbers.reverse()
            print('[' + ','.join(map(str, numbers)) + ']')
            break
