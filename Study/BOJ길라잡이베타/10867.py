#중복 빼고 정렬하기
N = input()

numbers = set(map(int, input().split()))

sorted(numbers)

print(*set(numbers))