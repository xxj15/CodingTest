import sys
input = sys.stdin.readline

nA, nB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

diff = sorted(A - B)  # 차집합 후 오름차순

print(len(diff))
if diff:
    print(*diff)
