#중복 빼고 정렬하기
N = input()

numbers = list(map(int, input().split()))

numbers.sort()

print(*set(numbers))