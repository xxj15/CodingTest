A, B, C = map(int, input().split())


def func(n):
    if n == 0:
        return 1
    num = func(n // 2)

    if n % 2 == 1:
        return A * num * num % C
    elif n % 2 == 0:
        return num * num % C


print(func(B))
