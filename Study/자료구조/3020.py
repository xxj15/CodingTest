#개똥벌레 
import sys
input = sys.stdin.readline

N, H = map(int, input().split())
lines = [0] * H # 구간별 충돌 횟수 기록 배열

for i in range(N):
    size = int(input())

    if i % 2 == 0: # 종유석
        lines[H-size] += 1

    else: # 석순
        lines[0] += 1
        lines[size] -= 1


for i in range(1, H):
    lines[i] += lines[i-1]

result = 0

low = min(lines)
for l in lines:

    if l == low:
        result += 1

print(low, result)

