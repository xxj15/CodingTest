N = int(input())
data = list(input() for _ in range(N))
ans = []
idx = 0

# while data[0] != 'KBS1' and data[1] != 'KBS2':
#     a = data.index('KBS1')

a = data.index('KBS1')
for _ in range(a):
    ans.append(1)
for _ in range(a):
    ans.append(4)
data[1:a+1] = data[0:a]
data[0]='KBS1'
b = data.index('KBS2')
for _ in range(b):
    ans.append(1)
for _ in range(b-1):
    ans.append(4)

for w in ans:
    print(w, end = '')