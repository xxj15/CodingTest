# 차집합
# 집합 A에는 속하면서 집합 B에는 속하지 않는 모든 원소를 구하기

nA, nB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

diff = sorted(A - B)  

print(len(diff))
if diff:
    print(*diff)
