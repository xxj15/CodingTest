n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0

def check_ishappy(seq):
    cnt = 1

    for i in range(1,n):
        if seq[i] == seq[i-1]:
            cnt += 1
            if cnt >= m:
                return 1
        else:
            cnt = 1
            if cnt >= m:
                return 1
    else:
        return 0


for i in range(n):
    data = grid[i][:]
    ans += check_ishappy(data)

for j in range(n):
    data = []
    for i in range(n):
        data.append(grid[i][j])
    
    ans += check_ishappy(data)

print(ans)